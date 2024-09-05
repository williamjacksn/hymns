import httpx
import pymupdf

revision = '2024.5.0'

h = 'https://assets.churchofjesuschrist.org'

cover = f'{h}/37/10/37108f66ca8411eeba3aeeeeac1ea51f5750182f/sacred_music.jpeg'

hymn_data = [
    {
        'blank_after': False,
        'number': 1001,
        'number_loc': 'r',
        'pdf_url': f'{h}/6e/4e/6e4ecd14ebb511ee863aeeeeac1eaa7887580260/come_thou_fount_of_every_blessing.pdf',
    },
    {
        'blank_after': False,
        'number': 1002,
        'number_loc': 'l',
        'pdf_url': f'{h}/70/a7/70a7ff54ebb511eeb4d5eeeeac1ea6754c802f3d/when_the_savior_comes_again.pdf',
    },
    {
        'blank_after': False,
        'number': 1003,
        'number_loc': 'l',
        'pdf_url': f'{h}/6f/d3/6fd34a32ebb511eea3b1eeeeac1e2cdd0ffc6784/it_is_well_with_my_soul.pdf',
    },
    {
        'blank_after': False,
        'number': 1004,
        'number_loc': 'l',
        'pdf_url': f'{h}/6f/cb/6fcb5af5ebb511ee903eeeeeac1e7de67f84090e/i_will_walk_with_jesus.pdf',
    },
    {
        'blank_after': False,
        'number': 1005,
        'number_loc': 'l',
        'pdf_url': f'{h}/6f/00/6f001bb4ebb511eea424eeeeac1e211e768ee551/his_eye_is_on_the_sparrow.pdf',
    },
    {
        'blank_after': False,
        'number': 1006,
        'number_loc': 'l',
        'pdf_url': f'{h}/70/39/703937f5ebb511ee888feeeeac1e36706b2e5f48/think_a_sacred_song.pdf',
    },
    {
        'blank_after': False,
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
        'blank_after': False,
        'number': 1009,
        'number_loc': 'l',
        'pdf_url': f'{h}/6e/79/6e795f87ebb511eebd27eeeeac1ef760eeedab62/gethsemane.pdf'
    },
    {
        'blank_after': False,
        'number': 1201,
        'number_loc': 'l',
        'pdf_url': f'{h}/6e/9f/6e9fac3debb511eea036eeeeac1ec84f90cdba38/hail_the_day_that_sees_him_rise.pdf'
    },
    {
        'blank_after': False,
        'number': 1202,
        'number_loc': 'r',
        'pdf_url': f'{h}/6e/d8/6ed86f77ebb511eeb141eeeeac1eae03688eebd1/he_is_born_the_divine_christ_child.pdf'
    },
    {
        'blank_after': False,
        'number': 1203,
        'number_loc': 'l',
        'pdf_url': f'{h}/70/73/707381d2ebb511eeb518eeeeac1e3b993d94e337/what_child_is_this.pdf'
    },
    {
        'blank_after': False,
        'number': 1204,
        'number_loc': 'l',
        'pdf_url': f'{h}/6f/fb/6ffbe0d8ebb511eeb958eeeeac1e769f17b3574f/star_bright.pdf'
    }
]

page_width = 495.0
page_height = 711.0

final = pymupdf.Document()

# intro pages
page = final.new_page(width=page_width, height=page_height)
img_rect = (page_width * 0.1, page_width * 0.3, page_width * 0.9, (page_width * 0.9) + (page_width * 0.2))
img_response = httpx.get(cover)
page.insert_image(img_rect, stream=img_response.content)
title_rect = (page_width * 0.1, page_width * 0.1, page_width * 0.9, page_width * 0.2)
page.insert_textbox(title_rect, 'Hymns\x97For Home and Church', fontsize=28, fontname='times-roman',
                    align=pymupdf.TEXT_ALIGN_CENTER)

final.new_page(width=page_width, height=page_height)

for hymn in hymn_data:
    url = hymn.get('pdf_url')
    response = httpx.get(url)
    doc = pymupdf.open(stream=response.content)
    page = doc[0]
    last_page_rect = page.rect
    if hymn.get('number_loc') == 'l':
        x = 37
    else:
        width = page.rect.width
        x = width - 70
    y = 48
    page.insert_text((x, y), str(hymn.get('number')), fontsize=18, fontname='Times-Roman')
    final.insert_pdf(doc)
    if hymn.get('blank_after'):
        final.new_page(width=page.rect.width, height=page.rect.height)
    doc.close()

page = final.new_page(width=page_width, height=page_height)
rect = pymupdf.Rect(0, page.rect.height * 0.9, page.rect.width, page.rect.height)
page.insert_textbox(rect, f'\nhttps://github.com/williamjacksn/hymns\nRevision {revision}', fontsize=8,
                    fontname='times-roman', align=pymupdf.TEXT_ALIGN_CENTER)
page.insert_link({
    'kind': pymupdf.LINK_URI,
    'from': rect,
    'uri': 'https://github.com/williamjacksn/hymns',
})

final.save('hymns.pdf')
final.close()
