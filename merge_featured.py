#!/usr/bin/env python3
"""Merge Science article screenshot with science logo for post featured image."""

from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("Install Pillow: pip install Pillow")

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
SCREENSHOT = Path(
    "/Users/knmnyn/.cursor/projects/Users-knmnyn-Desktop-git-wing-nus-wing-website/assets"
    "/Screenshot_2026-02-07_at_11.35.24-3102c38a-bf62-4873-8a77-b358da4c0118.png"
)
POST_DIR = SCRIPT_DIR / "content" / "post" / "26-02-04-science-commentary"
CURRENT_FEATURED = POST_DIR / "featured.jpg"
OUTPUT = POST_DIR / "featured.jpg"


def main():
    if not SCREENSHOT.exists():
        raise SystemExit(f"Screenshot not found: {SCREENSHOT}")

    base = Image.open(SCREENSHOT).convert("RGB")
    w, h = base.size

    # If we have the current featured with the science panel, extract science logo area
    if CURRENT_FEATURED.exists():
        featured = Image.open(CURRENT_FEATURED).convert("RGBA")
        fw, fh = featured.size
        # Left panel is ~1/3: "AI for SCIENCE" with brain and molecular icons
        left_third = fw // 3
        # Crop top portion with icons (roughly top 40%) to get logo strip
        science_logo = featured.crop((0, 0, left_third, int(fh * 0.45)))
        # Scale logo to ~20% of screenshot width for overlay
        logo_w = int(w * 0.22)
        ratio = logo_w / science_logo.width
        logo_h = int(science_logo.height * ratio)
        science_logo = science_logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
        # Paste at bottom-right with small margin
        margin = int(min(w, h) * 0.02)
        x = w - science_logo.width - margin
        y = h - science_logo.height - margin
        base.paste(science_logo, (x, y), science_logo)
    else:
        # No existing featured: use screenshot as-is (still save as featured.jpg)
        pass

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    base.save(OUTPUT, "JPEG", quality=88, optimize=True)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
