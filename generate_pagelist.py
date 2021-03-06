#!/usr/bin/env python3
#
# Generates a list of pages to export from Mediawiki by iterating through html files in the 'export' directory.
#

import re, os

def generate_pagelist():
    if os.path.exists('export/'):
        os.chdir('export/')
    else:
        os.makedirs('export/')
        os.chdir('export/')
    if os.path.exists('../pages.export'):
        os.remove('../pages.export')
    filename = open('../pages.export', 'a+')
    for i in os.listdir('.'):
        if i.endswith(".html"):
            content = open(str(i)).read()
            page_regex = re.findall('title="(\w.*?)"', content)
            print('Appending ' + i + ' to pages.export ...')
            filename.write("\n".join(page_regex))

    filename.close()

if __name__ == "__main__":
    generate_pagelist()

