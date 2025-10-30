#!/usr/bin/env python3

import os, re, shutil
from bs4 import BeautifulSoup   # pip install beautifulsoup4

# loop through every *.html file in the current directory
for fname in sorted(f for f in os.listdir('.') if f.endswith('.html')):
    with open(fname, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # get h1 text inside the .main-header-content-block
    h1 = soup.select_one('.main-header-content-block h1')
    if not h1:
        print(f"⚠️  No h1 found in {fname}, skipping.")
        continue

    text = h1.get_text(separator=' ', strip=True)

    # slugify for folder name
    slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    if not slug:
        print(f"⚠️  Empty slug for {fname}, skipping.")
        continue

    # create directory if it doesn’t exist
    
    os.makedirs(slug, exist_ok=True)

    # move and rename page to index.html

    dest = os.path.join(slug, 'index.html')
    shutil.move(fname, dest)
    print(f"{fname} → {dest}")
