import json 
import os 
import pandas as pd 
import argparse


class IndexLinking:
    def __init__(self, author_index_path, pub_dir, author_alias_path=None):
        self.author_index_path = author_index_path
        self.pub_dir = pub_dir
        # load the author_index_path
        with open(author_index_path, "r") as f:
            self.author_index = json.load(f)
        # load hand-maintained name variants (see assets/author_aliases.json).
        # author_index.json is regenerated from profile titles and holds one name
        # per slug, so former/alternative published names have to live separately.
        self.aliases = dict()
        if author_alias_path and os.path.isfile(author_alias_path):
            with open(author_alias_path, "r") as f:
                for alias_name, slug in json.load(f).items():
                    if alias_name.startswith('_'):
                        continue
                    if slug not in self.author_index:
                        print(f"WARNING: alias '{alias_name}' points at unknown slug '{slug}'; ignoring")
                        continue
                    self.aliases[alias_name] = slug

    def author_linking(self, query_name):
        # a hand-maintained alias wins over the generated index
        if query_name in self.aliases:
            return ['In Aliases', self.aliases[query_name]]
        # check if the author_id is in the author_index
        if query_name in self.author_index:
            return ['In Index', query_name]
        for name in self.author_index.values():
            if query_name == name:
                # Get the key of the name
                key = list(self.author_index.keys())[list(self.author_index.values()).index(name)]
                return ['In Value', key]
            
            # Following is for the case that the author name is not exactly the same as the author name in the index
            # get the subname of the query_name
            subname_q = query_name.split(' ')
            subname_n = name.split(' ')
            # get the set of subname_q and subname_n
            set_q = set(subname_q)
            set_n = set(subname_n)
            # check if the set_q is a subset of set_n
            if set_q.issubset(set_n):
                key = list(self.author_index.keys())[list(self.author_index.values()).index(name)]
                return ['In Value by Subset', key]
        return ['NOT FOUND', '']

    def loop_pub_dir(self):
        # loop through all subdirectories in the pub_dir
        for pub_id in os.listdir(self.pub_dir):
            if not os.path.isdir(os.path.join(self.pub_dir, pub_id)):
                continue
            # the actual page is index.md inside the pub_id directory
            page_path = os.path.join(self.pub_dir, pub_id, "index.md")
            print(page_path)
            # check if the page_path is a file
            if not os.path.isfile(page_path):
                continue
            # read the page
            with open(page_path, "r") as f:
                page_content = f.read()
            # Extract the title from the page content
            title_line = [line for line in page_content.split('\n') if line.startswith('title:')][0]
            title = title_line.replace('title:', '').strip()
            print('---------------')
            print(pub_id, title)

            # Extract the authors from the page content
            author_lines = dict()
            in_authors = False
            for line in page_content.split('\n'):
                if line.startswith('authors:'):
                    in_authors = True
                    continue
                if in_authors:
                    if line.startswith('-') or line.startswith('  -'):
                        # author_name = line.replace('-', '').strip()
                        # check if the first letter is '-', if so, remove it
                        if line[0] == '-':
                            line = line[1:].strip()
                        if line.startswith('  -'):
                            line = line[3:].strip()
                        author_status = self.author_linking(line)
                        # author_lines.append(author_name + ' (' + author_status[0] + ' ' + author_status[1] + ')'))
                        author_lines[line] = author_status[1]
                    else:
                        if not line.startswith(' '):
                            in_authors = False

            # Loop through each author
            # for author in author_lines:
                # print(f"  Author: {author}, {author_lines[author]}")

            print(author_lines)
            # Let's read the page_content again
            with open(page_path, "r") as f:
                page_content = f.read()
            
            for author_name, author_key in author_lines.items():
                # look for "- {author_name}\n"
                if f"- {author_name}\n" in page_content:
                    if len(author_key) > 0:
                        # replace the line with "- {author_key}\n"
                        page_content = page_content.replace(f"- {author_name}\n", f"- {author_key}\n")
                        print(f"Replaced {author_name} with {author_key}")

            # Write the page_content back to the page_path
            with open(page_path, "w") as f:
                f.write(page_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--author_index_path", type=str, default="assets/author_index.json")
    parser.add_argument("--author_alias_path", type=str, default="assets/author_aliases.json")
    parser.add_argument("--pub_dir", type=str, default="content/publication")
    args = parser.parse_args()

    index_linking = IndexLinking(args.author_index_path, args.pub_dir, args.author_alias_path)
    index_linking.loop_pub_dir()
