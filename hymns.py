import httpx
import io
import pathlib
import pymupdf
import qrcode

revision = '2024.5.1'
src_repo = 'https://github.com/williamjacksn/hymns'
hymns_homepage = 'https://www.churchofjesuschrist.org/media/music/collections/hymns-for-home-and-church'

h = 'https://assets.churchofjesuschrist.org'
cover_url = f'{h}/37/10/37108f66ca8411eeba3aeeeeac1ea51f5750182f/sacred_music.jpeg'
hymn_data = [
    {
        'number': 1001,
        'number_loc': 'r',
        'pdf_url': f'{h}/6e/4e/6e4ecd14ebb511ee863aeeeeac1eaa7887580260/come_thou_fount_of_every_blessing.pdf',
    },
    {
        'number': 1002,
        'number_loc': 'l',
        'pdf_url': f'{h}/70/a7/70a7ff54ebb511eeb4d5eeeeac1ea6754c802f3d/when_the_savior_comes_again.pdf',
    },
    {
        'number': 1003,
        'number_loc': 'l',
        'pdf_url': f'{h}/6f/d3/6fd34a32ebb511eea3b1eeeeac1e2cdd0ffc6784/it_is_well_with_my_soul.pdf',
    },
    {
        'number': 1004,
        'number_loc': 'l',
        'pdf_url': f'{h}/6f/cb/6fcb5af5ebb511ee903eeeeeac1e7de67f84090e/i_will_walk_with_jesus.pdf',
    },
    {
        'number': 1005,
        'number_loc': 'l',
        'pdf_url': f'{h}/6f/00/6f001bb4ebb511eea424eeeeac1e211e768ee551/his_eye_is_on_the_sparrow.pdf',
    },
    {
        'number': 1006,
        'number_loc': 'l',
        'pdf_url': f'{h}/70/39/703937f5ebb511ee888feeeeac1e36706b2e5f48/think_a_sacred_song.pdf',
    },
    {
        'number': 1007,
        'number_loc': 'r',
        'pdf_url': f'{h}/6d/f3/6df3dbd5ebb511eea9a7eeeeac1eca3ca4ff6c01/as_bread_is_broken.pdf',
    },
    {
        'blank_after': True,
        'number': 1008,
        'number_loc': 'l',
        'pdf_url': f'{h}/6e/06/6e062b55ebb511eeb343eeeeac1ef072e68df91f/bread_of_life_living_water.pdf',
    },
    {
        'number': 1009,
        'number_loc': 'l',
        'pdf_url': f'{h}/6e/79/6e795f87ebb511eebd27eeeeac1ef760eeedab62/gethsemane.pdf'
    },
    {
        'number': 1201,
        'number_loc': 'l',
        'pdf_url': f'{h}/6e/9f/6e9fac3debb511eea036eeeeac1ec84f90cdba38/hail_the_day_that_sees_him_rise.pdf'
    },
    {
        'number': 1202,
        'number_loc': 'r',
        'pdf_url': f'{h}/6e/d8/6ed86f77ebb511eeb141eeeeac1eae03688eebd1/he_is_born_the_divine_christ_child.pdf'
    },
    {
        'number': 1203,
        'number_loc': 'l',
        'pdf_url': f'{h}/70/73/707381d2ebb511eeb518eeeeac1e3b993d94e337/what_child_is_this.pdf'
    },
    {
        'number': 1204,
        'number_loc': 'l',
        'pdf_url': f'{h}/6f/fb/6ffbe0d8ebb511eeb958eeeeac1e769f17b3574f/star_bright.pdf'
    }
]

font = 'times-roman'
page_width = 495.0
page_height = 711.0

final = pymupdf.Document()

# intro pages
page = final.new_page(width=page_width, height=page_height)

title_rect = (page_width * 0.1, page_height * 0.05, page_width * 0.9, page_height * 0.15)
text = 'Hymns\x97For Home and Church'
page.insert_textbox(title_rect, text, fontsize=30, fontname=font)

img_rect = (page_width * 0.1, page_width * 0.2, page_width * 0.9, (page_width * 0.9) + (page_width * 0.1))
cover = pathlib.Path() / '.local/cache/cover.jpg'
if not cover.exists():
    cover.parent.mkdir(parents=True, exist_ok=True)
    img_response = httpx.get(cover_url)
    cover.write_bytes(img_response.content)
page.insert_image(img_rect, filename=cover.resolve())

link_rect = pymupdf.Rect(page_width * 0.1, page_height * 0.8, page_width * 0.9, page_height * 0.9)
text = f'Access these hymns digitally at\n{hymns_homepage}'
page.insert_textbox(link_rect, text, fontsize=10, fontname=font, align=pymupdf.TEXT_ALIGN_CENTER)
page.insert_link({
    'kind': pymupdf.LINK_URI,
    'from': link_rect,
    'uri': hymns_homepage,
})

qr_rect = pymupdf.Rect(page_width * 0.45, page_height * 0.85, page_width * 0.55, (page_height * 0.85) + (page_width * 0.1))
qr = qrcode.make(hymns_homepage)
qr_stream = io.BytesIO()
qr.save(qr_stream)
page.insert_image(qr_rect, stream=qr_stream)

page = final.new_page(width=page_width, height=page_height)
src_rect = pymupdf.Rect(0, page_height * 0.9, page_width, page_height)
text = f'\n{src_repo}\nRevision {revision}'
page.insert_textbox(src_rect, text, fontsize=8, fontname=font, align=pymupdf.TEXT_ALIGN_CENTER)
page.insert_link({
    'kind': pymupdf.LINK_URI,
    'from': src_rect,
    'uri': src_repo,
})

qr_rect = pymupdf.Rect(page_width * 0.45, page_height * 0.8, page_width * 0.55, (page_height * 0.8) + (page_width * 0.1))
qr = qrcode.make(src_repo)
qr_stream = io.BytesIO()
qr.save(qr_stream)
page.insert_image(qr_rect, stream=qr_stream)

# hymn pages
for hymn in hymn_data:
    cache_target = pathlib.Path() / f'.local/cache/{hymn.get('number')}.pdf'
    if not cache_target.exists():
        url = hymn.get('pdf_url')
        response = httpx.get(url)
        cache_target.parent.mkdir(parents=True, exist_ok=True)
        cache_target.write_bytes(response.content)
    doc = pymupdf.Document(cache_target)
    page = doc[0]
    if hymn.get('number_loc', 'l') == 'l':
        x = 37
    else:
        x = page.rect.width - 70
    y = 48
    page.insert_text((x, y), str(hymn.get('number')), fontsize=18, fontname=font)
    final.insert_pdf(doc)
    if hymn.get('blank_after', False):
        final.new_page(width=page_width, height=page_height)
    doc.close()

final.save('hymns.pdf')
final.close()
