#!/bin/env python3
#
# Scrapes files from the /tg/ wiki
#
# Usage: ./extract-images.py [URL]

import re
import urllib.request
import sys, os
import generate_pagelist
from bs4 import BeautifulSoup

# Fetches the pages we'll scrape and formats them.
def main():
    generate_pagelist.generate_pagelist()
    filename = open('../pages.export', 'r').read()
    articles_list = filename.splitlines()
    articles_formatted = []
    print(articles_list)
    for x in articles_list:
        articles_formatted.append("https://tgstation13.org/wiki/" + x)
    for meme in articles_formatted:
        nice(meme)

# Create directories, initialize everything.

def nice(meme):
    wiki_url = sys.argv[1]
    img_dir = '../extracted-images/'
    if os.path.exists("../extracted-images/"):
        os.chdir(img_dir)
        url_extract(meme)
    else:
        os.makedirs(img_dir)
        os.chdir(img_dir)
        url_extract(meme)

# Extract image urls from parsed html.

def url_extract(url):
    print('!! DOWNLOADING FROM ' + url + ' !!')
    response = urllib.request.urlopen(url, data=None)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    images = [img['src'] for img in soup.find_all('img')]

    format_attrs(images)


# Download our images via direct link.
def dl_from_array(images_formatted):
    for url in images_formatted:
        print("Retrieving " + url)
        filename = url.rsplit('/', 1)[-1]
        print("... \nSaving as " + filename)
        urllib.request.urlretrieve(url, filename)

# Append the image path to the url, forming a direct link to the image.
def format_attrs(images):
    images_formatted = []
    for img in images:
        images_formatted.append("https://tgstation13.org" + img)

    dl_from_array(images_formatted)

if __name__ == "__main__":
    main()
