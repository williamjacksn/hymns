"""List all paper sizes that are predefined in PyMuPDF."""

import pymupdf

format_col = 13
width_col = 5
height_col = 6


def print_line(fmt: str, width: str, height: str) -> None:
    print(
        fmt.rjust(format_col),
        "|",
        width.rjust(width_col),
        "|",
        height.rjust(height_col),
    )


print_line("format", "width", "height")
print("-" * 30)

for f, d in pymupdf.paper_sizes().items():
    print_line(f, str(d[0]), str(d[1]))
