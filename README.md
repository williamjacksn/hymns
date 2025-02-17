# Hymns

Use this project to compile a single PDF containing all the hymns in the collection [Hymns&mdash;For Home and Church][a].

[a]: https://www.churchofjesuschrist.org/media/music/collections/hymns-for-home-and-church?lang=eng

Running `hymns.py` will perform the following actions:

1.  Download PDF files for all hymns.
2.  Add hymn numbers to the first page of each hymn.
3.  Arrange all hymns into a single PDF file.
4.  Add blank pages if necessary to keep two-page hymns in a single spread.
5.  Write the combined PDF file to `hymns-eng-letter.pdf` in the current directory. If `hymns-eng-letter.pdf` already exists, it will be overwritten.

The resulting PDF is designed to be printed double-sided.

## Alternate languages and paper sizes

The default language is English. The default paper size is Letter (8.5 x 11 inches).

You can specify a different language or a different paper size by using `--lang` or `--size` when you run `hymns.py`:

```shell
> python hymns.py --lang spa --size a4
# or abbreviated:
> python hymns.py -l spa -s a4
```

Currently supported languages are:

* `eng`: English
* `spa`: Spanish

Currently supported paper sizes are:

* `letter`: 8.5 x 11 inches
* `a4`: 210 x 297 mm

You can generate all possible combinations of language and paper size by running:

```shell
> python gen-all.py
```

## Updating a printed copy

If you already have a printed copy of a previous version, you only need to print added or changed pages to update your copy.

### 2024.5 &rarr; 2024.9

* Print pages 1&ndash;2 to replace pages 1&ndash;2 in your existing copy.
* Print pages 17&ndash;36 to replace pages 17&ndash;18 in your existing copy.

### 2024.9 &rarr; 2025.2

* Print pages 1&ndash;2 to replace pages 1&ndash;2 in your existing copy.
* Print pages 35&ndash;60 to replace pages 35&ndash;36 in your existing copy.
* Print pages 67&ndash;69 to insert at the end of your existing copy.
