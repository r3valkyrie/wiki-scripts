#!/usr/bin/env python3
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
    with open('pages.export') as filename:
        filename_formatted = filename.read().replace(" ", "_")
    articles_list = filename_formatted.splitlines()
    articles_formatted = []
    print(articles_list)
    for x in articles_list:
        articles_formatted.append("https://tgstation13.org/wiki/" + x)
    for meme in articles_formatted:
        nice(meme)

# Create directories, initialize everything.

def nice(meme):
    # wiki_url = sys.argv[1] # Removing temporarily
    img_dir = os.path.dirname(os.path.realpath(__file__)) + "/extracted-images/"
    print(img_dir)
    if os.path.exists(img_dir):
        url_extract(meme, img_dir)
    else:
        os.makedirs(img_dir)
        url_extract(meme, img_dir)

# Extract image urls from parsed html.

def url_extract(url, img_dir):
    print('!! DOWNLOADING FROM ' + url + ' !!')
    response = urllib.request.urlopen(url, data=None)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    images = [img['src'] for img in soup.find_all('img')]

    format_attrs(images, img_dir)

# Append the image path to the url, forming a direct link to the image.
def format_attrs(images, img_dir):
    images_formatted = []
    for img in images:
        images_formatted.append("https://tgstation13.org" + img)

    dl_from_array(images_formatted, img_dir)

# Download our images via direct link.
def dl_from_array(images_formatted, img_dir):
    for url in images_formatted:
        filename = url.rsplit('/', 1)[-1]
        directory = img_dir + url.rsplit('/', 3)[-3] + '/' + url.rsplit('/', 2)[-2] + '/'
        print(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(directory + filename):
            print("... \nSaving " + filename + ' to directory ' + directory)
            urllib.request.urlretrieve(url, directory + filename)
        else:
            print('... \n' + directory + filename + " seems to exist, skipping...")


if __name__ == "__main__":
    main()
