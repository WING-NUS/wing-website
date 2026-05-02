#!/usr/bin/env python3
"""
Dead Link Checker for Hugo Website
Scans markdown and HTML files for links and checks if they're valid.
"""

import os
import re
import sys
import yaml
import requests
from pathlib import Path
from urllib.parse import urlparse, urljoin
from collections import defaultdict
import time

# Configuration
BASE_DIR = Path(__file__).parent
CONTENT_DIR = BASE_DIR / "content"
STATIC_DIR = BASE_DIR / "static"
TIMEOUT = 10  # seconds for HTTP requests
MAX_RETRIES = 2
DELAY_BETWEEN_REQUESTS = 0.5  # seconds to avoid rate limiting

# Track all links found
all_links = defaultdict(list)  # {url: [list of (file, line_number)]}
dead_links = []
checked_urls = {}  # Cache for URL checks

# Patterns for extracting links
MARKDOWN_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
HTML_LINK_PATTERN = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
HTML_IMG_PATTERN = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
SHORTCODE_LINK_PATTERN = re.compile(r'link=["\']([^"\']+)["\']', re.IGNORECASE)
YAML_URL_PATTERN = re.compile(r'url:\s*(.+)', re.IGNORECASE)

def is_external_url(url):
    """Check if URL is external (starts with http:// or https://)"""
    return url.startswith('http://') or url.startswith('https://')

def is_internal_link(url):
    """Check if URL is an internal link (relative path)"""
    return not is_external_url(url) and not url.startswith('#') and not url.startswith('mailto:')

def normalize_internal_path(url, base_file):
    """Convert relative path to absolute path"""
    if url.startswith('/'):
        # Absolute path from site root
        return BASE_DIR / url.lstrip('/')
    else:
        # Relative path
        base_dir = base_file.parent
        return (base_dir / url).resolve()

def check_internal_link(url, base_file):
    """Check if internal link exists"""
    try:
        path = normalize_internal_path(url, base_file)
        # Check if file exists
        if path.exists() and path.is_file():
            return True
        # Check if directory with index.md exists
        if path.is_dir() and (path / 'index.md').exists():
            return True
        # Check if it's a markdown file without extension
        if (path.parent / (path.name + '.md')).exists():
            return True
        # Check Hugo permalink patterns
        # For author links: /author/:slug/
        if url.startswith('author/') or '/author/' in url:
            author_slug = url.split('/')[-1].rstrip('/')
            author_path = CONTENT_DIR / 'authors' / author_slug / '_index.md'
            if author_path.exists():
                return True
        # For publication links
        if '/publication/' in url or url.startswith('publication/'):
            pub_slug = url.split('/')[-1].rstrip('/')
            pub_path = CONTENT_DIR / 'publication' / pub_slug / 'index.md'
            if pub_path.exists():
                return True
        return False
    except Exception as e:
        return False

def check_external_url(url):
    """Check if external URL is accessible"""
    if url in checked_urls:
        return checked_urls[url]
    
    try:
        # Skip certain URLs that might cause issues
        if any(skip in url.lower() for skip in ['localhost', '127.0.0.1', 'example.com', 'example.org']):
            checked_urls[url] = (True, "Skipped (example/localhost)")
            return True, "Skipped"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; LinkChecker/1.0)'
        }
        
        response = requests.head(url, timeout=TIMEOUT, headers=headers, allow_redirects=True)
        status_ok = response.status_code < 400
        
        # Some servers don't support HEAD, try GET
        if response.status_code == 405:
            response = requests.get(url, timeout=TIMEOUT, headers=headers, allow_redirects=True, stream=True)
            status_ok = response.status_code < 400
        
        checked_urls[url] = (status_ok, f"Status {response.status_code}")
        time.sleep(DELAY_BETWEEN_REQUESTS)  # Be polite
        return status_ok, f"Status {response.status_code}"
    except requests.exceptions.Timeout:
        checked_urls[url] = (False, "Timeout")
        return False, "Timeout"
    except requests.exceptions.ConnectionError:
        checked_urls[url] = (False, "Connection Error")
        return False, "Connection Error"
    except requests.exceptions.TooManyRedirects:
        checked_urls[url] = (False, "Too Many Redirects")
        return False, "Too Many Redirects"
    except Exception as e:
        checked_urls[url] = (False, str(e))
        return False, str(e)

def extract_yaml_links(content, file_path):
    """Extract links from YAML frontmatter"""
    links = []
    try:
        # Split frontmatter from content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                try:
                    data = yaml.safe_load(frontmatter)
                    if data:
                        # Check for url fields
                        for key in ['url', 'url_pdf', 'url_code', 'url_dataset', 'url_poster', 
                                   'url_project', 'url_slides', 'url_source', 'url_video']:
                            if key in data and data[key] and data[key] != '#':
                                links.append((data[key], file_path, f"YAML:{key}"))
                        # Check for links array
                        if 'links' in data and isinstance(data['links'], list):
                            for link_item in data['links']:
                                if isinstance(link_item, dict) and 'url' in link_item:
                                    url = link_item['url']
                                    if url and url != '#':
                                        links.append((url, file_path, "YAML:links"))
                except yaml.YAMLError:
                    pass
    except Exception:
        pass
    return links

def extract_links_from_file(file_path):
    """Extract all links from a file"""
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Extract from YAML frontmatter
        yaml_links = extract_yaml_links(content, file_path)
        links.extend(yaml_links)
        
        # Extract markdown links
        for line_num, line in enumerate(lines, 1):
            for match in MARKDOWN_LINK_PATTERN.finditer(line):
                url = match.group(2)
                if url and url != '#':
                    links.append((url, file_path, line_num))
            
            # Extract HTML links
            for match in HTML_LINK_PATTERN.finditer(line):
                url = match.group(1)
                if url and url != '#':
                    links.append((url, file_path, line_num))
            
            # Extract from shortcodes (Hugo figure shortcode)
            for match in SHORTCODE_LINK_PATTERN.finditer(line):
                url = match.group(1)
                if url and url != '#':
                    links.append((url, file_path, line_num))
        
        # Extract HTML img src (might be links)
        for line_num, line in enumerate(lines, 1):
            for match in HTML_IMG_PATTERN.finditer(line):
                url = match.group(1)
                if url and not url.startswith('data:'):
                    links.append((url, file_path, line_num))
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
    
    return links

def scan_directory(directory, pattern="*.md"):
    """Scan directory for files matching pattern"""
    files = []
    for root, dirs, filenames in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for filename in filenames:
            if filename.endswith('.md') or filename.endswith('.html'):
                files.append(Path(root) / filename)
    return files

def main():
    print("🔍 Scanning for links...")
    
    # Scan markdown files in content directory
    md_files = scan_directory(CONTENT_DIR)
    print(f"Found {len(md_files)} markdown files in content/")
    
    # Scan HTML files in static directory
    html_files = scan_directory(STATIC_DIR)
    print(f"Found {len(html_files)} HTML files in static/")
    
    all_files = md_files + html_files
    
    # Extract all links
    print("\n📝 Extracting links from files...")
    for file_path in all_files:
        links = extract_links_from_file(file_path)
        for url, source_file, location in links:
            all_links[url].append((source_file, location))
    
    print(f"Found {len(all_links)} unique links")
    
    # Check links
    print("\n🔗 Checking links...")
    internal_links = []
    external_links = []
    
    for url, occurrences in all_links.items():
        if is_external_url(url):
            external_links.append((url, occurrences))
        elif is_internal_link(url):
            internal_links.append((url, occurrences))
    
    print(f"  - {len(internal_links)} internal links")
    print(f"  - {len(external_links)} external links")
    
    # Check internal links
    print("\n📂 Checking internal links...")
    dead_internal = []
    for url, occurrences in internal_links:
        # Use first occurrence's file as base
        base_file = occurrences[0][0]
        if not check_internal_link(url, base_file):
            dead_internal.append((url, occurrences))
    
    # Check external links
    print("\n🌐 Checking external links...")
    dead_external = []
    for i, (url, occurrences) in enumerate(external_links, 1):
        print(f"  Checking {i}/{len(external_links)}: {url[:60]}...", end='\r')
        is_valid, reason = check_external_url(url)
        if not is_valid:
            dead_external.append((url, occurrences, reason))
    
    print()  # New line after progress
    
    # Report results
    print("\n" + "="*80)
    print("📊 LINK CHECK RESULTS")
    print("="*80)
    
    if not dead_internal and not dead_external:
        print("\n✅ All links are valid!")
        return 0
    
    if dead_internal:
        print(f"\n❌ Found {len(dead_internal)} dead internal link(s):")
        print("-" * 80)
        for url, occurrences in dead_internal:
            print(f"\n  Link: {url}")
            for source_file, location in occurrences:
                print(f"    - {source_file} ({location})")
    
    if dead_external:
        print(f"\n❌ Found {len(dead_external)} dead external link(s):")
        print("-" * 80)
        for url, occurrences, reason in dead_external:
            print(f"\n  Link: {url}")
            print(f"    Reason: {reason}")
            for source_file, location in occurrences:
                print(f"    - {source_file} ({location})")
    
    print("\n" + "="*80)
    return 1

if __name__ == "__main__":
    sys.exit(main())
