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


def get_qr(text: str):
    qr = qrcode.make(text, image_factory=qrcode.image.pure.PyPNGImage)
    qr_stream = io.BytesIO()
    qr.save(qr_stream)
    return qr_stream


def main():
    font = 'times-roman'
    # This is the page size used by Church PDFs
    page_width = 495.0  #  6.875"
    page_height = 711.0  # 9.875"

    final = pymupdf.Document()

    # intro pages
    page = pymupdf.utils.new_page(final, width=page_width, height=page_height)

    title_rect = (page_width * 0.1, page_height * 0.05, page_width * 0.9, page_height * 0.15)
    # left aligned due to the extra wide \x97 char which messes up center algo
    pymupdf.utils.insert_textbox(page, title_rect, data.eng.title, fontname=font, fontsize=31)

    img_rect = (page_width * 0.1, page_width * 0.2, page_width * 0.9, (page_width * 0.9) + (page_width * 0.1))
    cover = pathlib.Path() / '.local/cache/cover.jpg'
    if not cover.exists():
        cover.parent.mkdir(parents=True, exist_ok=True)
        print(f'Downloading {cover_url}')
        img_response = httpx.get(cover_url)
        cover.write_bytes(img_response.content)
    pymupdf.utils.insert_image(page, img_rect, filename=cover.resolve())

    link_rect = pymupdf.Rect(page_width * 0.1, page_height * 0.8, page_width * 0.9, page_height * 0.9)
    pymupdf.utils.insert_textbox(page, link_rect, data.eng.hymn_link_text, fontname=font, fontsize=12, align=pymupdf.TEXT_ALIGN_CENTER)
    pymupdf.utils.insert_link(page, {
        'from': link_rect,
        'kind': pymupdf.LINK_URI,
        'uri': data.eng.hymns_homepage,
    })

    qr_rect = pymupdf.Rect(page_width * 0.45, page_height * 0.85, page_width * 0.55, (page_height * 0.85) + (page_width * 0.1))
    pymupdf.utils.insert_image(page, qr_rect, stream=get_qr(data.eng.hymns_homepage))

    page = pymupdf.utils.new_page(final, width=page_width, height=page_height)
    text = f'\n{data.eng.rev_text} {revision}'
    pymupdf.utils.insert_textbox(page, link_rect, text, fontname=font, fontsize=8, align=pymupdf.TEXT_ALIGN_CENTER)
    pymupdf.utils.insert_link(page, {
        'from': link_rect,
        'kind': pymupdf.LINK_URI,
        'uri': src_repo,
    })

    pymupdf.utils.insert_image(page, qr_rect, stream=get_qr(src_repo))

    # hymn pages
    for hymn in data.eng.hymns:
        cache_target = pathlib.Path() / f'.local/cache/{data.eng.lang}/{hymn.number}.pdf'
        if not cache_target.exists():
            url = hymn.pdf_url
            print(f'Downloading {url}')
            response = httpx.get(url)
            cache_target.parent.mkdir(parents=True, exist_ok=True)
            cache_target.write_bytes(response.content)
        doc = pymupdf.Document(cache_target)
        page = doc[0]
        if hymn.num_on_left:
            x = 37
        else:
            x = page.rect.width - 70
        y = 48
        pymupdf.utils.insert_text(page, (x, y), str(hymn.number), fontsize=18, fontname=font)
        if hymn.blank_before:
            pymupdf.utils.new_page(final, width=page_width, height=page_height)
        final.insert_pdf(doc)
        doc.close()

    # resize to letter paper (sadly, this will drop the links)
    resized_doc = pymupdf.Document()

    letter_width, letter_height = pymupdf.paper_size('letter')  # (612, 792) = 8.5"x11.0"
    for src_page in final:
        dst_page = pymupdf.utils.new_page(resized_doc, width=letter_width, height=letter_height)
        if pymupdf.utils.get_text(src_page):
            pymupdf.utils.show_pdf_page(dst_page, dst_page.rect, final, src_page.number)

    resized_doc.save('hymns-letter.pdf')
    resized_doc.close()
    final.save('hymns.pdf')
    final.close()


if __name__ == '__main__':
    main()
