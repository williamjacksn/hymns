import dataclasses

h = 'https://assets.churchofjesuschrist.org'


@dataclasses.dataclass
class Hymn:
    number: int
    asset_path: str
    num_on_left: bool = True
    blank_before: bool = False
    excluded_pages: list[int] = dataclasses.field(default_factory=list)
    custom_num_position: tuple[float, float] = None

    @property
    def pdf_url(self) -> str:
        return f'{h}/{self.asset_path}'


@dataclasses.dataclass
class DocData:
    hymns: list[Hymn]
    title: str = 'Hymns\x97For Home and Church'
    title_font_size: int = 38
    hymn_link_text: str = '\nScan this code to access these hymns digitally'
    rev_text: str = 'Revision'
    lang: str = 'eng'

    @property
    def hymns_homepage(self) -> str:
        return f'https://www.churchofjesuschrist.org/media/music/collections/hymns-for-home-and-church?lang={self.lang}'


# noinspection SpellCheckingInspection
eng = DocData([
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
])

# noinspection SpellCheckingInspection
fra = DocData(
    [
        Hymn(1001, '30/c4/30c4a2d0073c11efb5e6eeeeac1e9990cd1dd5d0/come_thou_fount_of_every_blessing.pdf', False),
        Hymn(1002, '2b/b7/2bb7b116097f11ef89a1eeeeac1e46f4a20eedc4/when_the_savior_comes_again.pdf'),
        Hymn(1003, '28/83/28836118097f11ef882feeeeac1e4505adb519b9/it_is_well_with_my_soul.pdf'),
        Hymn(1004, '27/af/27af6f44097f11ef9554eeeeac1e2f439219cbca/i_will_walk_with_jesus.pdf'),
        Hymn(1005, '26/00/2600d4e7097f11efac44eeeeac1e90496a2e9fad/his_eye_is_on_the_sparrow.pdf'),
        Hymn(1006, '2a/21/2a213296097f11efad51eeeeac1e84248ac0cf8a/think_a_sacred_song.pdf'),
        Hymn(1007, '21/8c/218c3cb4097f11ef88d1eeeeac1ed719c52a4f34/as_bread_is_broken.pdf', False, excluded_pages=[1]),
        Hymn(1008, '22/eb/22eb0963097f11efa109eeeeac1e70a58a6b7d86/bread_of_life_living_water.pdf', False, True),
        Hymn(1009, '23/8a/238aa4c9097f11ef8a5aeeeeac1e3b9fcdbd0309/gethsemane.pdf'),
        Hymn(1010, 'y3/7m/y37m057bd41ku7ifo58q7ry1spgk13qk7duxr8l4/amazing_grace.pdf', False, True),
        Hymn(1011, '26/ed/26ed09a6097f11efa04beeeeac1ed97cd3b2787d/holding_hands_around_the_world.pdf'),
        Hymn(1012, 'or/lf/orlfd3mf3clkpfto7pdywfxpel9bmidbtpecnu2s/anytime_anywhere.pdf', False, True),
        Hymn(1013, 'gi/hi/gihiqq3209ffpau17frji60efsgq61rljixxgos5/gods_gracious_love.pdf'),
        Hymn(1014, '9v/mn/9vmndz16d9l9h7l2zr3wtp122ypr5i8yjy427s13/my_shepherd_will_supply_my_need.pdf'),
        Hymn(1015, 'hp/xf/hpxfkr5dzxbw92hwj9vqsduwh0sbo150jetjdx50/oh_the_deep_deep_love_of_jesus.pdf', False, True),
        Hymn(1016, 'a6/ux/a6uxtghps14i4ssoozcejgs9cibasyq6odo6pdxr/behold_the_wounds_in_jesus_hands.pdf'),
        Hymn(1017, '7q/zp/7qzpq1vulnt4n4l9arsex718dezssq7bw8obd1bc/this_is_the_christ.pdf'),
        Hymn(1018, 'mm/vi/mmvisbiiw57dvknkaeb8n0qwo2fftbv5sfnvwxtp/come_lord_jesus.pdf'),
        Hymn(1019, 'g6/1i/g61im34xzkp4g57lkpulstl8s13ia5d3z837t8mp/to_love_like_thee.pdf', False, True),
        Hymn(1020, 'gp/9w/gp9wrc3mo329pfa8awa8rmend5zil6tstukclxls/softly_and_tenderly_jesus_is_calling.pdf'),
        Hymn(1021, '8q/wa/8qwassgx63hy67boll7v4e52ro459q4d0lzxvs2w/i_cant_count_them_all.pdf'),
        Hymn(1022, 'yi/jw/yijwjtstvopci0avkh4ol8l823nobcqptlfcxvn9/faith_in_every_footstep.pdf'),
        Hymn(1023, 'lv/8d/lv8dpnyjrmynmua154j1fvkv7f1n9a2ykizdmk8b/standing_on_the_promises.pdf'),
        Hymn(1024, '8o/d6/8od657vpjqxyhzjiv95vjr5ixxdqfycxzdmozezi/i_have_faith_in_the_lord_jesus_christ.pdf'),
        Hymn(1025, 'jc/kp/jckptf6savvxab34ny5dbcv2236h3g1gld5vt09r/take_my_heart_and_let_it_be_consecrated.pdf'),
        Hymn(1026, 'nu/81/nu81fvjq9ab9f2d9t8i1owhqpgm60tq1343inec7/holy_places.pdf', False),
        Hymn(1027, '05/s0/05s0daaceszp9yp01jmthqmuamg9231u7o3mih2q/welcome_home.pdf'),
        Hymn(1028, 'uk/lw/uklwlgmummoix6b65m2301gh0ylcmpz6j43b0swo/this_little_light_of_mine.pdf'),
        Hymn(1029, '7n/6i/7n6irgk6xct34xz18hf8xtu27wmzbnce48gs2ljb/i_cant_count_them_all.pdf', False),
        Hymn(1030, 'yn/ge/yngevzb1vct2puwrd4bmvreo3jfdeidixqu2293v/close_as_a_quiet_prayer.pdf'),
        Hymn(1031, 'pt/z7/ptz77oj92sut1n1rp20cyu0fl11z8ffvwxd42lwi/come_hear_the_word_the_lord_has_spoken.pdf', False, True),
        Hymn(1201, '24/78/2478120a097f11efae13eeeeac1e705949a29d62/hail_the_day_that_sees_him_rise.pdf', False, True),
        Hymn(1202, '80/04/800459b10e8611efa950eeeeac1ef0d0090f76f2/he_is_born_the_divine_christ_child.pdf', False, True, custom_num_position=(0.82, 0.137)),
        Hymn(1203, '2a/d4/2ad4f232097f11efabb0eeeeac1e06f99913c180/what_child_is_this.pdf'),
        Hymn(1204, '29/45/29450364097f11efb9ceeeeeac1ed262191adfc5/star_bright.pdf'),
        Hymn(1205, 'd8/4o/d84ogspp8cp0nnzfe9n6cmsjscziveuxvtfb40bt/let_easter_anthems_ring.pdf', False, True),
        Hymn(1206, '9a/90/9a9067jxwg1y0rkf58wzwvqhkax8oyrh2xvbgzmf/were_you_there.pdf'),
    ],
    title='Cantiques \x96 Pour le foyer et l\x92église',
    title_font_size=34,
    hymn_link_text='\nScannez ce code pour accéder à ces hymnes numériquement',
    rev_text='Révision',
    lang='fra'
)

# noinspection SpellCheckingInspection
spa = DocData(
    [
        Hymn(1001, 'c2/84/c284c254073b11efbfd2eeeeac1e0cc7c94404a1/come_thou_fount_of_every_blessing.pdf', False),
        Hymn(1002, '6b/9b/6b9b7f4b0ca311ef8fc9eeeeac1e0de2bbf1578f/when_the_savior_comes_again.pdf'),
        Hymn(1003, '61/2d/612daab80ca311ef9be7eeeeac1ec3fd60ec888c/it_is_well_with_my_soul.pdf'),
        Hymn(1004, '60/96/609625ac0ca311efa648eeeeac1e2f5955fd268c/i_will_walk_with_jesus.pdf'),
        Hymn(1005, '5e/a3/5ea3565f0ca311efb941eeeeac1ef7cfdf0191ba/his_eye_is_on_the_sparrow.pdf'),
        Hymn(1006, '69/dc/69dcdf5b0ca311ef8e16eeeeac1ea134e1752487/think_a_sacred_song.pdf'),
        Hymn(1007, '5a/54/5a546e9b0ca311ef80a4eeeeac1e1a8976dcfe6c/as_bread_is_broken.pdf', False),
        Hymn(1008, '5b/4c/5b4c8a3f0ca311efaf3ceeeeac1e008b2ff6cee6/bread_of_life_living_water.pdf', False, True),
        Hymn(1009, '5c/2a/5c2ab53a0ca311ef8fc9eeeeac1e0de2710d4e06/gethsemane.pdf'),
        Hymn(1010, 'rj/md/rjmdkfwcvyj40z9x5mptv3rlp3mjq0r3f2ajvz3o/amazing_grace.pdf', False, True),
        Hymn(1011, '5f/cd/5fcd576f0ca311efb82eeeeeac1e03e733245bc0/holding_hands_around_the_world.pdf'),
        Hymn(1012, 'ie/jk/iejkdwj6ogfhn6gcok301zck7s0vgbe1ch5ltiqa/anytime_anywhere.pdf', False, True),
        Hymn(1013, 'zu/nl/zunlwr8mxkcfs1kgwcupi3y2kyhds082vokow4e3/gods_gracious_love.pdf'),
        Hymn(1014, 'w1/z8/w1z84shlyiaxdiv3dz98f2otmp1h8g11qxiaooxl/my_shepherd_will_supply_my_need.pdf'),
        Hymn(1015, '27/fo/27fo18n3uiobq291iegxy2j3j96rqc73g5mmavfb/oh_the_deep_deep_love_of_jesus.pdf', False, True),
        Hymn(1016, '1d/cb/1dcbgah3w40qzk0yj2mw2mqbi9mxjohrzo0t9z1r/behold_the_wounds_in_jesus_hands.pdf'),
        Hymn(1017, 'k1/r6/k1r6w3qrec4frhpd9uv7xqst2ds3qqihw2k2ebwe/this_is_the_christ.pdf'),
        Hymn(1018, 'af/6a/af6acu0yilofg8ir3okj65ok0dzgj4pztjbz9rvt/come_lord_jesus.pdf'),
        Hymn(1019, 'v9/3m/v93moe9wq88u72jcegrml14tiay33yhelzi1u14c/to_love_like_thee.pdf', False, True),
        Hymn(1020, 'dd/lr/ddlron658e7ddvysueq896d705ocaiegkyctm79l/softly_and_tenderly_jesus_is_calling.pdf'),
        Hymn(1021, 'qq/z5/qqz5xu4ml313y9y5zc9ddrtjh2v0dy4p0a7oetcm/i_cant_count_them_all.pdf'),
        Hymn(1022, 'nf/y0/nfy0b6o8a8nict43hjiw8wouzhygzq1j8n0r0xb9/faith_in_every_footstep.pdf'),
        Hymn(1023, 'od/gb/odgbnqo5s3xtpj1gfuj4o0cexj494dznmynhzroz/standing_on_the_promises.pdf'),
        Hymn(1024, '7a/5j/7a5josf3w4uqvia5kid7d25e7qbi41h48bg2va4b/i_have_faith_in_the_lord_jesus_christ.pdf'),
        Hymn(1025, 'm4/hx/m4hxp2k110signsnn2og7nuvlzitpqsf56oujb8k/take_my_heart_and_let_it_be_consecrated.pdf'),
        Hymn(1026, 'm4/t2/m4t2kz3s1cm4qirncmy6c5u99v27hm6sysib5y5g/holy_places.pdf', False),
        Hymn(1027, '2f/03/2f0382g3csuryqk8ed6fyc7eyav2m14hig9475t1/welcome_home.pdf'),
        Hymn(1028, '5y/hb/5yhb3bx04vzoib9knwtkwrqlkgutxvphb6e6wo4c/this_little_light_of_mine.pdf'),
        Hymn(1029, 'td/3c/td3crppjmqvown4gld4jt294zy5u7sg01i79su78/i_cant_count_them_all.pdf', False),
        Hymn(1030, '1s/dw/1sdw6aog5dz1o7bdcsd8ymtd5gfldd433ha552e3/close_as_a_quiet_prayer.pdf'),
        Hymn(1031, 'dd/hx/ddhx8cggoprf726m2fro8xfj7l97fzqsyv9df4w8/come_hear_the_word_the_lord_has_spoken.pdf', False, True),
        Hymn(1201, '5d/1e/5d1e15ee0ca311efb82eeeeeac1e03e79b85b9b2/hail_the_day_that_sees_him_rise.pdf', False, True),
        Hymn(1202, '5d/ba/5dbacb230ca311ef823ceeeeac1ea7cf84767a94/he_is_born_the_divine_christ_child.pdf', False, True),
        Hymn(1203, '6a/de/6ade49c60ca311ef89fbeeeeac1e28fb7942f974/what_child_is_this.pdf'),
        Hymn(1204, '80/02/8002fa220e8611efb3baeeeeac1e55fa95392dc5/star_bright.pdf'),
        Hymn(1205, 'ac/au/acauj22rj8p1prejn4zq4w5v00x0ygkk9mzk47rx/let_easter_anthems_ring.pdf', False, True),
        Hymn(1206, 'v3/gd/v3gd4rag00g44u16ik7v8noshtwt94gq6uc2law8/were_you_there.pdf'),
    ],
    title='Himnos \x97 Para el hogar y la Iglesia',
    title_font_size=33,
    hymn_link_text='\nEscanee este código para acceder los himnos digitalmente',
    rev_text='Revisión',
    lang='spa'
)
