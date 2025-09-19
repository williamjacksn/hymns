import argparse

import pymupdf

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

doc = pymupdf.open(args.file)
page = doc[0]
print(page.rect.width, page.rect.height)
