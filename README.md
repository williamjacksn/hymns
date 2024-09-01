# hymns

Use this project to compile a single PDF containing all the hymns in the collection [Hymns&mdash;For Home and Church][a].

[a]: https://www.churchofjesuschrist.org/media/music/collections/hymns-for-home-and-church?lang=eng

Running `hymns.py` will perform the following actions:

1.  Download PDF files for all hymns.
2.  Add hymn numbers to the first page of each hymn.
3.  Arrange all hymns into a single PDF file.
4.  Add blank pages if necessary to keep two-page hymns in a single spread.
5.  Write the combined PDF file to `hymns.pdf` in the current directory.

If `hymns.pdf` already exists, it will be overwritten.
