import argparse
import importlib.metadata
import io
import itertools
import pathlib

import httpx
import pymupdf
import qrcode.image.pure

from . import data

revision = importlib.metadata.version("hymns")
src_repo = importlib.metadata.metadata("hymns").get("Project-URL").split(", ")[1]

# noinspection SpellCheckingInspection
cover_url = f"{data.h}/37/10/37108f66ca8411eeba3aeeeeac1ea51f5750182f/sacred_music.jpeg"

lang_choices = data.lang_map.keys()
size_choices = ["a4", "letter"]


class Args:
    lang: str = "eng"
    size: str = "letter"


def parse_args() -> Args:
    parser = argparse.ArgumentParser(
        description="Compile a single PDF containing all the hymns in the collection "
        '"Hymns—For Home and Church".',
        epilog=f"Visit {src_repo} for more information.",
    )
    parser.add_argument(
        "-l",
        "--lang",
        default="eng",
        choices=lang_choices,
        help="language (default: eng)",
    )
    parser.add_argument(
        "-s",
        "--size",
        default="letter",
        choices=size_choices,
        help="paper size (default: letter)",
    )
    ns = Args()
    return parser.parse_args(namespace=ns)


def get_qr(text: str) -> io.BytesIO:
    qr = qrcode.make(text, image_factory=qrcode.image.pure.PyPNGImage)
    qr_stream = io.BytesIO()
    qr.save(qr_stream)
    return qr_stream


def build_pdf(language: str, paper_size: str) -> None:
    doc_data = data.lang_map.get(language, data.eng.doc_data)

    page_width, page_height = pymupdf.paper_size(paper_size)
    font = "times-roman"
    final = pymupdf.Document()

    # intro pages
    link_rect = pymupdf.Rect(
        page_width * 0.1, page_height * 0.8, page_width * 0.9, page_height * 0.9
    )
    qr_rect = pymupdf.Rect(
        page_width * 0.45,
        page_height * 0.85,
        page_width * 0.55,
        (page_height * 0.85) + (page_width * 0.1),
    )

    # cover page
    page = final.new_page(width=page_width, height=page_height)
    title_rect = (
        page_width * 0.1,
        page_height * 0.05,
        page_width * 0.9,
        page_height * 0.15,
    )
    # left aligned due to the extra wide \x97 char which messes up center algo
    page.insert_textbox(
        title_rect,
        doc_data.title,
        fontname=font,
        fontsize=doc_data.title_font_size(paper_size),
    )

    img_rect = (
        page_width * 0.1,
        page_width * 0.2,
        page_width * 0.9,
        (page_width * 0.9) + (page_width * 0.1),
    )
    cover = pathlib.Path(".local/cache/cover.jpg").resolve()
    if cover.exists():
        print(f"Using cache: {cover}")
    else:
        cover.parent.mkdir(parents=True, exist_ok=True)
        print(f"Downloading {cover_url}")
        print(f" -> {cover}")
        img_response = httpx.get(cover_url)
        cover.write_bytes(img_response.content)
    page.insert_image(img_rect, filename=cover)

    text = f"\n{doc_data.hymn_link_text}"
    page.insert_textbox(
        link_rect, text, fontname=font, fontsize=12, align=pymupdf.TEXT_ALIGN_CENTER
    )
    page.insert_link(
        {"from": link_rect, "kind": pymupdf.LINK_URI, "uri": doc_data.hymns_homepage}
    )

    page.insert_image(qr_rect, stream=get_qr(doc_data.hymns_homepage))

    # github link page
    page = final.new_page(width=page_width, height=page_height)
    text = f"\n{doc_data.rev_text} {revision}"
    page.insert_textbox(
        link_rect, text, fontname=font, fontsize=8, align=pymupdf.TEXT_ALIGN_CENTER
    )
    page.insert_link({"from": link_rect, "kind": pymupdf.LINK_URI, "uri": src_repo})

    page.insert_image(qr_rect, stream=get_qr(src_repo))

    # hymn pages
    for hymn in doc_data.hymns:
        cache_target = pathlib.Path(
            f".local/cache/{doc_data.lang}/{hymn.number}.pdf"
        ).resolve()
        if cache_target.exists():
            print(f"Using cache: {cache_target}")
        else:
            url = hymn.pdf_url
            print(f"Downloading {url}")
            print(f" -> {cache_target}")
            response = httpx.get(url)
            cache_target.parent.mkdir(parents=True, exist_ok=True)
            cache_target.write_bytes(response.content)
        doc = pymupdf.Document(cache_target)
        if hymn.blank_before:
            final.new_page(width=page_width, height=page_height)
        for page in doc:
            if page.number + 1 in hymn.excluded_pages:
                continue
            new_page = final.new_page(width=page_width, height=page_height)
            new_page.show_pdf_page(new_page.rect, doc, page.number)
            if page.number == 0:
                point = (
                    page_width * hymn.x(paper_size),
                    page_height * hymn.y(paper_size),
                )
                new_page.insert_text(
                    point, str(hymn.number), fontsize=20, fontname=font
                )
        doc.close()

    final.save(f"hymns-{doc_data.lang}-{paper_size}.pdf")
    final.close()


def gen_all() -> None:
    for lang, size in itertools.product(lang_choices, size_choices):
        print(f"Generating document for lang:{lang} and size:{size}")
        build_pdf(lang, size)


def main() -> None:
    args = parse_args()
    build_pdf(args.lang, args.size)


if __name__ == "__main__":
    main()
