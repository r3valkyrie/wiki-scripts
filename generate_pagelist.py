#!/bin/env python3
#
# Generates a list of pages to export from Mediawiki by iterating through html files in the 'export' directory.
#

import re, os

def main():
    file_contents = []
    for i in os.listdir('export/'):
        if i.endswith(".html"):
            content = open(str(i)).read()
            findSpecialPages = re.compile('title="(\w.*?)"').findall
            file_contents.append(findSpecialPages)
        print(file_contents)




if __name__ == "__main__":
    main()
