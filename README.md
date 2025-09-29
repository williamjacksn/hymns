# Hymns

Use this package to compile a single PDF containing all the hymns in the collection
[Hymns&mdash;For Home and Church][a].

[a]: https://www.churchofjesuschrist.org/media/music/collections/hymns-for-home-and-church

## Using this tool

You do not need to download the source code repository to use this package. The
recommended way to use this package is to run it through `uv`. [Install `uv`][b] on your
computer and then run:

[b]: https://docs.astral.sh/uv/getting-started/installation/

```shell
uvx hymns
```

This will perform the following actions:

1.  Download PDF files for all hymns into a folder named `.local/cache` in the current
    directory.
2.  Add hymn numbers to the first page of each hymn, in the correct corner.
3.  Arrange all hymns into a single PDF file.
4.  Add blank pages if necessary to keep two-page hymns in a single spread.
5.  Write the combined PDF file to `hymns-eng-letter.pdf` in the current directory. If
    `hymns-eng-letter.pdf` already exists, it will be overwritten.

The resulting PDF is designed to be printed double-sided.

## Alternate languages and paper sizes

The default language is English. The default paper size is Letter (8.5 x 11 inches).

You can specify a different language or a different paper size by using `--lang` or
`--size` when you run `uvx hymns`:

```shell
> uvx hymns --lang spa --size a4
# or abbreviated:
> uvx hymns -l spa -s a4
```

Currently supported languages are:

* `eng`: English
* `fra`: French
* `por`: Portuguese (Brazil)
* `spa`: Spanish

Currently supported paper sizes are:

* `letter`: 8.5 x 11 inches
* `a4`: 210 x 297 mm

You can generate all possible combinations of language and paper size by running:

```shell
> uvx --from hymns gen-all-hymns
```

## Cover image

The official cover image for this new collection of hymns as found at
[the Church&#x02bc;s website][a] is legally protected.

> The Church&#x02bc;s wordmark and symbol are to be used only as approved by the First
> Presidency and Quorum of the Twelve Apostles. They may not be used as decorative
> elements. Nor may they be used in any personal, commercial, or promotional way.
> ([_General Handbook_, 38.8.8][c])

[c]: https://www.churchofjesuschrist.org/study/manual/general-handbook/38-church-policies-and-guidelines#title_number143

To include the cover image on the first page of the generated file, you can use
`--cover` when you run `uvx hymns`:

```shell
> uvx hymns --cover
# or abbreviated
> uvx hymns -c
```

## Updating a printed copy

If you already have a printed copy of a previous version, you only need to print added
or changed pages to update your copy.

### 2024.5 &rarr; 2024.9

* Print pages 1&ndash;2 to replace pages 1&ndash;2 in your existing copy.
* Print pages 17&ndash;36 to replace pages 17&ndash;18 in your existing copy.

### 2024.9 &rarr; 2025.2

* Print pages 1&ndash;2 to replace pages 1&ndash;2 in your existing copy.
* Print pages 35&ndash;60 to replace pages 35&ndash;36 in your existing copy.
* Print pages 67&ndash;69 to insert at the end of your existing copy.

### 2025.2 &rarr; 2025.6

* Print pages 1&ndash;2 to replace pages 1&ndash;2 in your existing copy.
* Print pages 55&ndash;70 to replace pages 55&ndash;58 in your existing copy.
* Print page 83 to insert at the end of your existing copy.

### 2025.6 &rarr; 2025.9

* Print pages 1&ndash;2 to replace pages 1&ndash;2 in your existing copy.
* Print pages 71&ndash;84 to insert after page 70 in your existing copy.
* Print pages 95&ndash;99 to replace pages 81&ndash;83 in your existing copy.

## Downloaded files

Any files that need to be downloaded to generate the final PDF will be saved in
a directory named `.local/cache` inside the current directory. If files already
exist in the cache folder, they will not be downloaded again.

You can safely delete this folder and everything in it. The next time you use this tool,
the files will be downloaded again.
