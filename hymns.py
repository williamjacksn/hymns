import argparse
import data
import httpx
import io
import pathlib
import pymupdf
import qrcode.image.pure


revision = '2025.2.1'
src_repo = 'https://github.com/williamjacksn/hymns'

# noinspection SpellCheckingInspection
cover_url = f'{data.h}/37/10/37108f66ca8411eeba3aeeeeac1ea51f5750182f/sacred_music.jpeg'

lang_choices = ['eng', 'spa']
size_choices = ['a4', 'letter']


class Args:
    lang: str = 'eng'
    size: str = 'letter'
    cover: bool = False


def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lang', default='eng', choices=lang_choices)
    parser.add_argument('-s', '--size', default='letter', choices=size_choices)
    parser.add_argument('-c', '--cover', action='store_true')
    ns = Args()
    return parser.parse_args(namespace=ns)


def get_qr(text: str):
    qr = qrcode.make(text, image_factory=qrcode.image.pure.PyPNGImage)
    qr_stream = io.BytesIO()
    qr.save(qr_stream)
    return qr_stream


def build_pdf(language: str, page_size: str, cover: bool = False):
    doc_data = data.eng
    if language == 'spa':
        doc_data = data.spa

    page_width, page_height = pymupdf.paper_size(page_size)
    font = 'times-roman'
    final = pymupdf.Document()

    # intro pages
    link_rect = pymupdf.Rect(page_width * 0.1, page_height * 0.8, page_width * 0.9, page_height * 0.9)
    qr_rect = pymupdf.Rect(page_width * 0.45, page_height * 0.85, page_width * 0.55, (page_height * 0.85) + (page_width * 0.1))

    # cover page
    page = pymupdf.utils.new_page(final, width=page_width, height=page_height)
    title_rect = (page_width * 0.1, page_height * 0.05, page_width * 0.9, page_height * 0.15)
    # left aligned due to the extra wide \x97 char which messes up center algo
    pymupdf.utils.insert_textbox(page, title_rect, doc_data.title, fontname=font, fontsize=doc_data.title_font_size)

    if cover:
        img_rect = (page_width * 0.1, page_width * 0.2, page_width * 0.9, (page_width * 0.9) + (page_width * 0.1))
        cover = pathlib.Path() / '.local/cache/cover.jpg'
        if not cover.exists():
            cover.parent.mkdir(parents=True, exist_ok=True)
            print(f'Downloading {cover_url}')
            img_response = httpx.get(cover_url)
            cover.write_bytes(img_response.content)
        pymupdf.utils.insert_image(page, img_rect, filename=cover.resolve())

    pymupdf.utils.insert_textbox(page, link_rect, doc_data.hymn_link_text, fontname=font, fontsize=12, align=pymupdf.TEXT_ALIGN_CENTER)
    pymupdf.utils.insert_link(page, {
        'from': link_rect,
        'kind': pymupdf.LINK_URI,
        'uri': doc_data.hymns_homepage,
    })

    pymupdf.utils.insert_image(page, qr_rect, stream=get_qr(doc_data.hymns_homepage))

    # github link page
    page = pymupdf.utils.new_page(final, width=page_width, height=page_height)
    text = f'\n{doc_data.rev_text} {revision}'
    pymupdf.utils.insert_textbox(page, link_rect, text, fontname=font, fontsize=8, align=pymupdf.TEXT_ALIGN_CENTER)
    pymupdf.utils.insert_link(page, {
        'from': link_rect,
        'kind': pymupdf.LINK_URI,
        'uri': src_repo,
    })

    pymupdf.utils.insert_image(page, qr_rect, stream=get_qr(src_repo))

    # hymn pages
    for hymn in doc_data.hymns:
        cache_target = pathlib.Path() / f'.local/cache/{doc_data.lang}/{hymn.number}.pdf'
        if not cache_target.exists():
            url = hymn.pdf_url
            print(f'Downloading {url}')
            response = httpx.get(url)
            cache_target.parent.mkdir(parents=True, exist_ok=True)
            cache_target.write_bytes(response.content)
        doc = pymupdf.Document(cache_target)
        if hymn.blank_before:
            pymupdf.utils.new_page(final, width=page_width, height=page_height)
        for page in doc:
            new_page = pymupdf.utils.new_page(final, width=page_width, height=page_height)
            pymupdf.utils.show_pdf_page(new_page, new_page.rect, doc, page.number)
            if page.number == 0:
                if hymn.num_on_left:
                    x = page_width * 0.11
                else:
                    x = page_width * 0.82
                y = page_height * 0.067
                pymupdf.utils.insert_text(new_page, (x, y), str(hymn.number), fontsize=20, fontname=font)
        doc.close()

    final.save(f'hymns-{doc_data.lang}-{page_size}.pdf')
    final.close()


if __name__ == '__main__':
    args = parse_args()
    build_pdf(args.lang, args.size, args.cover)
