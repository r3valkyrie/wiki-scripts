#!/bin/env python3
#
# Extracts image urls from provided urls, then downloads each image to a directory.
#
# Usage: ./extract-images.py [URL]
#

import re
import urllib.request
import sys, os
import generate_pagelist
from bs4 import BeautifulSoup

def dl_from_array(images_formatted):
    for url in images_formatted:
        print("Retrieving " + url)
        filename = url.rsplit('/', 1)[-1]
        print("... \nSaving as " + filename)
        urllib.request.urlretrieve(url, filename)

def format_attrs(images):
    images_formatted = []
    for img in images:
        images_formatted.append("https://tgstation13.org" + img)

    dl_from_array(images_formatted)

def url_extract(url):
    response = urllib.request.urlopen(url, data=None)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    images = [img['src'] for img in soup.find_all('img')]

    format_attrs(images)

def main():
    wiki_url = sys.argv[1]
    img_dir = '../extracted-images/'
    generate_pagelist.generate_pagelist()
    if os.path.exists("../extracted-images/"):
        os.chdir(img_dir)
        url_extract(wiki_url)
    else:
        os.makedirs(img_dir)
        os.chdir(img_dir)
        url_extract(wiki_url)


if __name__ == "__main__":
    main()
