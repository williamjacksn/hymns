import dataclasses
import httpx
import io
import pathlib
import pymupdf
import qrcode.image.pure


revision = '2025.2.1'
src_repo = 'https://github.com/williamjacksn/hymns'
hymns_homepage = 'https://www.churchofjesuschrist.org/media/music/collections/hymns-for-home-and-church'
h = 'https://assets.churchofjesuschrist.org'

# noinspection SpellCheckingInspection
cover_url = f'{h}/37/10/37108f66ca8411eeba3aeeeeac1ea51f5750182f/sacred_music.jpeg'


@dataclasses.dataclass
class Hymn:
    number: int
    asset_path: str
    num_on_left: bool = True
    blank_before: bool = False

    @property
    def pdf_url(self) -> str:
        return f'{h}/{self.asset_path}'


# noinspection SpellCheckingInspection
hymn_data = [
    Hymn(1001, '6e/4e/6e4ecd14ebb511ee863aeeeeac1eaa7887580260/come_thou_fount_of_every_blessing.pdf', False),
    Hymn(1002, '70/a7/70a7ff54ebb511eeb4d5eeeeac1ea6754c802f3d/when_the_savior_comes_again.pdf'),
    Hymn(1003, '6f/d3/6fd34a32ebb511eea3b1eeeeac1e2cdd0ffc6784/it_is_well_with_my_soul.pdf'),
    Hymn(1004, '6f/cb/6fcb5af5ebb511ee903eeeeeac1e7de67f84090e/i_will_walk_with_jesus.pdf'),
    Hymn(1005, '6f/00/6f001bb4ebb511eea424eeeeac1e211e768ee551/his_eye_is_on_the_sparrow.pdf'),
    Hymn(1006, '70/39/703937f5ebb511ee888feeeeac1e36706b2e5f48/think_a_sacred_song.pdf'),
    Hymn(1007, '6d/f3/6df3dbd5ebb511eea9a7eeeeac1eca3ca4ff6c01/as_bread_is_broken.pdf', False),
    Hymn(1008, '6e/06/6e062b55ebb511eeb343eeeeac1ef072e68df91f/bread_of_life_living_water.pdf', False, True),
    Hymn(1009, '6e/79/6e795f87ebb511eebd27eeeeac1ef760eeedab62/gethsemane.pdf'),
    Hymn(1010, 'oh/5v/oh5v0ejqfx70w7i6aq4bvhl1e9plpoyld9mk331x/amazing_grace.pdf', False, True),
    Hymn(1011, '6f/37/6f37cd82ebb511eebbd6eeeeac1e993e0630c9ee/holding_hands_around_the_world.pdf'),
    Hymn(1012, 'kn/rv/knrvba9apal6ivg0fo1u332xpvv9jhvdl4lg7yik/anytime_anywhere.pdf', False, True),
    Hymn(1013, 'md/4f/md4f9a3ntjzegeiqu52w4x3g2yt733eydjv63ep5/gods_gracious_love.pdf'),
    Hymn(1014, '8d/vf/8dvfxy75bz6w764yerum41314ynuwg7dqn6wkxa0/my_shepherd_will_supply_my_need.pdf'),
    Hymn(1015, 'nk/kl/nkklkoxo47tg4g8ev5sifeha39r6eipa55evuupy/oh_the_deep_deep_love_of_jesus.pdf', False, True),
    Hymn(1016, 'ou/qn/ouqn58wbc3ieqcnvdi38gbym6co5tejigxinfaw2/behold_the_wounds_in_jesus_hands.pdf'),
    Hymn(1017, 'z5/bf/z5bf1f2266jq08sp0l13nbbijbwl6kad9ze836sd/this_is_the_christ.pdf'),
    Hymn(1018, 'ib/hy/ibhyon46m2ibnt1synq1yaeciqqft4ef1h17xb44/come_lord_jesus.pdf'),
    Hymn(1019, 'jb/ni/jbniwxerq9gpvsubg55yk2ym1mczb3jt0xzohzry/to_love_like_thee.pdf', False, True),
    Hymn(1020, '6a/5o/6a5oag5khmdh2ssecgqgqrd3vnwsta9jqo1z0z9n/softly_and_tenderly_jesus_is_calling.pdf'),
    Hymn(1021, 'fn/bv/fnbvm8jbmrn47ug6qbu0eu6dwunucay4ljkqk1e2/i_know_that_my_savior_loves_me.pdf'),
    Hymn(1022, '3j/s4/3js483x1nxmpouv32y3awvi77x108p44c6a9907s/faith_in_every_footstep.pdf'),
    Hymn(1023, '79/ta/79tasqd6cffgga673rdaffgqe050d5dexf8z101i/standing_on_the_promises.pdf'),
    Hymn(1024, 'rz/hd/rzhd1yskdtpndjchivbyr2b9mf7gmlerlik6dgtu/i_have_faith_in_the_lord_jesus_christ.pdf'),
    Hymn(1025, 'ii/ox/iioxw8p3civdmchb71pw21v5zu5cozmyy7lx6ueq/take_my_heart_and_let_it_be_consecrated.pdf'),
    Hymn(1026, 'fq/wd/fqwdqbzjmdbivv679bzezgr47h28xb8qz0yg32l0/holy_places.pdf', False),
    Hymn(1027, 'eq/uh/equhtieoxfdjgdldggamp4nw74jz8ub6pvrpbb3q/welcome_home.pdf'),
    Hymn(1028, 'c9/6u/c96ux9no50moe9a1s57oy4gm1kcr2dk1cu0drci2/this_little_light_of_mine.pdf'),
    Hymn(1029, 'fl/gz/flgzaf0vovtww2p97xbsqsmmxtlyuzamowaz980b/i_cant_count_them_all.pdf', False),
    Hymn(1030, '95/6c/956cqf7l7rwugkycu2sp6s47vcxd0l8sil0bqb7d/close_as_a_quiet_prayer.pdf'),
    Hymn(1031, 'o8/wi/o8wigqygh5dll0mxq6qvegfy9gbcu8815uxpbic1/come_hear_the_word_the_lord_has_spoken.pdf', False, True),
    Hymn(1201, '6e/9f/6e9fac3debb511eea036eeeeac1ec84f90cdba38/hail_the_day_that_sees_him_rise.pdf', False, True),
    Hymn(1202, '6e/d8/6ed86f77ebb511eeb141eeeeac1eae03688eebd1/he_is_born_the_divine_christ_child.pdf', False, True),
    Hymn(1203, '70/73/707381d2ebb511eeb518eeeeac1e3b993d94e337/what_child_is_this.pdf'),
    Hymn(1204, '6f/fb/6ffbe0d8ebb511eeb958eeeeac1e769f17b3574f/star_bright.pdf'),
    Hymn(1205, '8z/nn/8znn69tb6fr1h2ctl0nkswt7ma8lc80jlklepyd6/let_easter_anthems_ring.pdf', False, True),
    Hymn(1206, '35/d0/35d0uc1i13madxx6wzlecpu3347lv09uebqrs75o/were_you_there.pdf'),
]


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
    text = 'Hymns\x97For Home and Church'
    # left aligned due to the extra wide \x97 char which messes up center algo
    pymupdf.utils.insert_textbox(page, title_rect, text, fontname=font, fontsize=31)

    img_rect = (page_width * 0.1, page_width * 0.2, page_width * 0.9, (page_width * 0.9) + (page_width * 0.1))
    cover = pathlib.Path() / '.local/cache/cover.jpg'
    if not cover.exists():
        cover.parent.mkdir(parents=True, exist_ok=True)
        print(f'Downloading {cover_url}')
        img_response = httpx.get(cover_url)
        cover.write_bytes(img_response.content)
    pymupdf.utils.insert_image(page, img_rect, filename=cover.resolve())

    link_rect = pymupdf.Rect(page_width * 0.1, page_height * 0.8, page_width * 0.9, page_height * 0.9)
    text = '\nScan this code to access these hymns digitally'
    pymupdf.utils.insert_textbox(page, link_rect, text, fontname=font, fontsize=12, align=pymupdf.TEXT_ALIGN_CENTER)
    pymupdf.utils.insert_link(page, {
        'from': link_rect,
        'kind': pymupdf.LINK_URI,
        'uri': hymns_homepage,
    })

    qr_rect = pymupdf.Rect(page_width * 0.45, page_height * 0.85, page_width * 0.55, (page_height * 0.85) + (page_width * 0.1))
    pymupdf.utils.insert_image(page, qr_rect, stream=get_qr(hymns_homepage))

    page = pymupdf.utils.new_page(final, width=page_width, height=page_height)
    text = f'\nRevision {revision}'
    pymupdf.utils.insert_textbox(page, link_rect, text, fontname=font, fontsize=8, align=pymupdf.TEXT_ALIGN_CENTER)
    pymupdf.utils.insert_link(page, {
        'from': link_rect,
        'kind': pymupdf.LINK_URI,
        'uri': src_repo,
    })

    pymupdf.utils.insert_image(page, qr_rect, stream=get_qr(src_repo))

    # hymn pages
    for hymn in hymn_data:
        cache_target = pathlib.Path() / f'.local/cache/{hymn.number}.pdf'
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
