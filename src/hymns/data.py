import dataclasses

h = "https://assets.churchofjesuschrist.org"


class DefaultOffsets:
    @staticmethod
    def x(num_on_left: bool, paper_size: str) -> float:
        if paper_size == "a4":
            if num_on_left:
                return 0.075
            else:
                return 0.857
        else:
            if num_on_left:
                return 0.11
            else:
                return 0.82

    @staticmethod
    def y(paper_size: str) -> float:
        return 0.067


@dataclasses.dataclass
class Hymn:
    number: int
    asset_path: str
    num_on_left: bool = True
    blank_before: bool = False
    excluded_pages: list[int] = dataclasses.field(default_factory=list)
    offsets: dict[str, tuple[float, float]] = dataclasses.field(default_factory=dict)

    @property
    def pdf_url(self) -> str:
        return f"{h}/{self.asset_path}"

    def x(self, paper_size: str = "letter") -> float:
        if paper_size in self.offsets:
            return self.offsets.get(paper_size)[0]
        else:
            return DefaultOffsets.x(self.num_on_left, paper_size)

    def y(self, paper_size: str = "letter") -> float:
        if paper_size in self.offsets:
            return self.offsets.get(paper_size)[1]
        else:
            return DefaultOffsets.y(paper_size)


@dataclasses.dataclass
class DocData:
    hymns: list[Hymn]
    title: str = "Hymns\x97For Home and Church"
    t_font_size: dict[str, int] = dataclasses.field(default_factory=dict)
    hymn_link_text: str = "Scan this code to access these hymns digitally"
    rev_text: str = "Revision"
    lang: str = "eng"

    @property
    def hymns_homepage(self) -> str:
        return f"https://www.churchofjesuschrist.org/media/music/collections/hymns-for-home-and-church?lang={self.lang}"

    def title_font_size(self, paper_size: str) -> int:
        if paper_size in self.t_font_size:
            return self.t_font_size.get(paper_size)
        if paper_size == "a4":
            return 37
        return 38


# noinspection SpellCheckingInspection
eng = DocData(
    [
        Hymn(
            1001,
            "6e/4e/6e4ecd14ebb511ee863aeeeeac1eaa7887580260/come_thou_fount_of_every_blessing.pdf",
            False,
        ),
        Hymn(
            1002,
            "70/a7/70a7ff54ebb511eeb4d5eeeeac1ea6754c802f3d/when_the_savior_comes_again.pdf",
        ),
        Hymn(
            1003,
            "6f/d3/6fd34a32ebb511eea3b1eeeeac1e2cdd0ffc6784/it_is_well_with_my_soul.pdf",
        ),
        Hymn(
            1004,
            "6f/cb/6fcb5af5ebb511ee903eeeeeac1e7de67f84090e/i_will_walk_with_jesus.pdf",
        ),
        Hymn(
            1005,
            "6f/00/6f001bb4ebb511eea424eeeeac1e211e768ee551/his_eye_is_on_the_sparrow.pdf",
        ),
        Hymn(
            1006,
            "70/39/703937f5ebb511ee888feeeeac1e36706b2e5f48/think_a_sacred_song.pdf",
        ),
        Hymn(
            1007,
            "6d/f3/6df3dbd5ebb511eea9a7eeeeac1eca3ca4ff6c01/as_bread_is_broken.pdf",
            False,
        ),
        Hymn(
            1008,
            "6e/06/6e062b55ebb511eeb343eeeeac1ef072e68df91f/bread_of_life_living_water.pdf",
            False,
            True,
        ),
        Hymn(1009, "6e/79/6e795f87ebb511eebd27eeeeac1ef760eeedab62/gethsemane.pdf"),
        Hymn(
            1010,
            "oh/5v/oh5v0ejqfx70w7i6aq4bvhl1e9plpoyld9mk331x/amazing_grace.pdf",
            False,
            True,
        ),
        Hymn(
            1011,
            "6f/37/6f37cd82ebb511eebbd6eeeeac1e993e0630c9ee/holding_hands_around_the_world.pdf",
        ),
        Hymn(
            1012,
            "kn/rv/knrvba9apal6ivg0fo1u332xpvv9jhvdl4lg7yik/anytime_anywhere.pdf",
            False,
            True,
        ),
        Hymn(
            1013,
            "md/4f/md4f9a3ntjzegeiqu52w4x3g2yt733eydjv63ep5/gods_gracious_love.pdf",
        ),
        Hymn(
            1014,
            "8d/vf/8dvfxy75bz6w764yerum41314ynuwg7dqn6wkxa0/my_shepherd_will_supply_my_need.pdf",
        ),
        Hymn(
            1015,
            "nk/kl/nkklkoxo47tg4g8ev5sifeha39r6eipa55evuupy/oh_the_deep_deep_love_of_jesus.pdf",
            False,
            True,
        ),
        Hymn(
            1016,
            "ou/qn/ouqn58wbc3ieqcnvdi38gbym6co5tejigxinfaw2/behold_the_wounds_in_jesus_hands.pdf",
        ),
        Hymn(
            1017,
            "z5/bf/z5bf1f2266jq08sp0l13nbbijbwl6kad9ze836sd/this_is_the_christ.pdf",
        ),
        Hymn(
            1018, "ib/hy/ibhyon46m2ibnt1synq1yaeciqqft4ef1h17xb44/come_lord_jesus.pdf"
        ),
        Hymn(
            1019,
            "jb/ni/jbniwxerq9gpvsubg55yk2ym1mczb3jt0xzohzry/to_love_like_thee.pdf",
            False,
            True,
        ),
        Hymn(
            1020,
            "6a/5o/6a5oag5khmdh2ssecgqgqrd3vnwsta9jqo1z0z9n/softly_and_tenderly_jesus_is_calling.pdf",
        ),
        Hymn(
            1021,
            "fn/bv/fnbvm8jbmrn47ug6qbu0eu6dwunucay4ljkqk1e2/i_know_that_my_savior_loves_me.pdf",
        ),
        Hymn(
            1022,
            "3j/s4/3js483x1nxmpouv32y3awvi77x108p44c6a9907s/faith_in_every_footstep.pdf",
        ),
        Hymn(
            1023,
            "79/ta/79tasqd6cffgga673rdaffgqe050d5dexf8z101i/standing_on_the_promises.pdf",
        ),
        Hymn(
            1024,
            "rz/hd/rzhd1yskdtpndjchivbyr2b9mf7gmlerlik6dgtu/i_have_faith_in_the_lord_jesus_christ.pdf",
        ),
        Hymn(
            1025,
            "ii/ox/iioxw8p3civdmchb71pw21v5zu5cozmyy7lx6ueq/take_my_heart_and_let_it_be_consecrated.pdf",
        ),
        Hymn(
            1026,
            "fq/wd/fqwdqbzjmdbivv679bzezgr47h28xb8qz0yg32l0/holy_places.pdf",
            False,
        ),
        Hymn(1027, "eq/uh/equhtieoxfdjgdldggamp4nw74jz8ub6pvrpbb3q/welcome_home.pdf"),
        Hymn(
            1028,
            "c9/6u/c96ux9no50moe9a1s57oy4gm1kcr2dk1cu0drci2/this_little_light_of_mine.pdf",
        ),
        Hymn(
            1029,
            "fl/gz/flgzaf0vovtww2p97xbsqsmmxtlyuzamowaz980b/i_cant_count_them_all.pdf",
            False,
        ),
        Hymn(
            1030,
            "95/6c/956cqf7l7rwugkycu2sp6s47vcxd0l8sil0bqb7d/close_as_a_quiet_prayer.pdf",
        ),
        Hymn(
            1031,
            "o8/wi/o8wigqygh5dll0mxq6qvegfy9gbcu8815uxpbic1/come_hear_the_word_the_lord_has_spoken.pdf",
        ),
        Hymn(
            1032,
            "ks/iq/ksiqaqmbw5d73vtpbvjl9i1hwp1991hezj80z10t/look_unto_christ.pdf",
            False,
        ),
        Hymn(
            1033,
            "1j/kg/1jkgot13zdk5ij9ir1gvw785bvi5jkafom5knwov/oh_how_great_is_our_joy.pdf",
        ),
        Hymn(
            1034, "fk/hv/fkhv4f39s3sgbrkzjj891iak4st1fagrycdge7m9/im_a_pioneer_too.pdf"
        ),
        Hymn(
            1035,
            "87/af/87aferimm4bh9h1asmajpvlnx902w98ehjpfv577/as_i_keep_the_sabbath_day.pdf",
            False,
        ),
        Hymn(
            1036,
            "vj/vq/vjvqnfv5f0180jmyzm8oewrmiu61hl2vykalwm56/read_the_book_of_mormon_and_pray.pdf",
        ),
        Hymn(
            1037,
            "af/ny/afny05n5s6xkznyrhv4vqdjnh76qs1576vjahmwo/im_gonna_live_so_god_can_use_me.pdf",
        ),
        Hymn(
            1038,
            "wg/rf/wgrfga1tcvxx56agz3lh62apy67aofyu6yhhgf2b/the_lords_my_shepherd.pdf",
            False,
        ),
        Hymn(1039, "l8/aa/l8aa8iq55nwm4ppvfm3qcr34oi81as8jwngih6kp/because.pdf"),
        Hymn(
            1040,
            "r6/rl/r6rli8pz3gawtj2f9bf9144ubs1zjlt4j6bxbcwl/his_voice_as_the_sound.pdf",
        ),
        Hymn(
            1041,
            "cj/oh/cjohf082cbp6pbodqau3zm9i9gmi4i3yk8hzdtsy/o_lord_who_gave_thy_life_for_me.pdf",
        ),
        Hymn(
            1042,
            "he/86/he86n6sqvar4ysrork5belj8fh33pbo914om83a9/thou_gracious_god_whose_mercy_lends.pdf",
            False,
        ),
        Hymn(
            1043, "mr/ii/mrii3sw2leivfi17lixh2v43i9pk1q73whpo9szo/help_us_remember.pdf"
        ),
        Hymn(
            1044,
            "28/35/28358y5wthp49fr4l0y3igtij3fnm2m0crxitxjd/how_did_the_savior_minister.pdf",
            False,
        ),
        Hymn(
            1045, "wg/82/wg82l7rydm9uzmnhw73gb77kdc6rny669trfwd6h/jesus_is_the_way.pdf"
        ),
        Hymn(
            1046,
            "ai/ln/ailn1tipdgc7out8odgcag8447od5u017ug3y7ou/can_you_count_the_stars_in_heaven.pdf",
        ),
        Hymn(
            1047,
            "x5/pa/x5pa1fa3sc3rkd6h679gaoprntum2j3ixl56ukpy/he_cares_for_me.pdf",
            False,
        ),
        Hymn(
            1048,
            "k4/hg/k4hg4muphm8mhqj8sb9eypt6yxv0edbb7w0upnlx/our_prayer_to_thee.pdf",
        ),
        Hymn(
            1049,
            "em/a0/ema0yxz439lqcgqevi4hy75cn9p55vxq9rb8wt4n/joseph_prayed_in_faith.pdf",
        ),
        Hymn(1050, "9x/3j/9x3jwrluybs3w8irtxo9e4mxdz39tqayhm7cmbm5/stand_by_me.pdf"),
        Hymn(
            1051,
            "9v/mm/9vmmfbdua2bpgmhufmx51o29itb8soq7bwowhf73/this_day_is_a_good_day_lord.pdf",
            False,
        ),
        Hymn(
            1201,
            "6e/9f/6e9fac3debb511eea036eeeeac1ec84f90cdba38/hail_the_day_that_sees_him_rise.pdf",
            False,
            True,
        ),
        Hymn(
            1202,
            "6e/d8/6ed86f77ebb511eeb141eeeeac1eae03688eebd1/he_is_born_the_divine_christ_child.pdf",
            False,
            True,
        ),
        Hymn(
            1203,
            "70/73/707381d2ebb511eeb518eeeeac1e3b993d94e337/what_child_is_this.pdf",
        ),
        Hymn(1204, "6f/fb/6ffbe0d8ebb511eeb958eeeeac1e769f17b3574f/star_bright.pdf"),
        Hymn(
            1205,
            "8z/nn/8znn69tb6fr1h2ctl0nkswt7ma8lc80jlklepyd6/let_easter_anthems_ring.pdf",
            False,
            True,
        ),
        Hymn(1206, "35/d0/35d0uc1i13madxx6wzlecpu3347lv09uebqrs75o/were_you_there.pdf"),
        Hymn(
            1207, "2z/gf/2zgfzovjzxpf440zhrjzixmxrmvih0r8b9h7sdnf/still_still_still.pdf"
        ),
        Hymn(
            1208,
            "cz/23/cz23g18i6a1kufdab9szptg26rq3j0kxhy2nfiod/go_tell_it_on_the_mountain.pdf",
            False,
        ),
        Hymn(
            1209,
            "jr/vl/jrvlt8nplnk8dejytlbilk8ej156pw22nfs7tdrm/little_baby_in_a_manger.pdf",
        ),
    ]
)


# noinspection SpellCheckingInspection
fra = DocData(
    [
        Hymn(
            1001,
            "30/c4/30c4a2d0073c11efb5e6eeeeac1e9990cd1dd5d0/come_thou_fount_of_every_blessing.pdf",
            False,
        ),
        Hymn(
            1002,
            "2b/b7/2bb7b116097f11ef89a1eeeeac1e46f4a20eedc4/when_the_savior_comes_again.pdf",
        ),
        Hymn(
            1003,
            "28/83/28836118097f11ef882feeeeac1e4505adb519b9/it_is_well_with_my_soul.pdf",
        ),
        Hymn(
            1004,
            "27/af/27af6f44097f11ef9554eeeeac1e2f439219cbca/i_will_walk_with_jesus.pdf",
        ),
        Hymn(
            1005,
            "26/00/2600d4e7097f11efac44eeeeac1e90496a2e9fad/his_eye_is_on_the_sparrow.pdf",
        ),
        Hymn(
            1006,
            "2a/21/2a213296097f11efad51eeeeac1e84248ac0cf8a/think_a_sacred_song.pdf",
        ),
        Hymn(
            1007,
            "21/8c/218c3cb4097f11ef88d1eeeeac1ed719c52a4f34/as_bread_is_broken.pdf",
            False,
            excluded_pages=[2],
        ),
        Hymn(
            1008,
            "22/eb/22eb0963097f11efa109eeeeac1e70a58a6b7d86/bread_of_life_living_water.pdf",
            False,
            True,
        ),
        Hymn(1009, "23/8a/238aa4c9097f11ef8a5aeeeeac1e3b9fcdbd0309/gethsemane.pdf"),
        Hymn(
            1010,
            "y3/7m/y37m057bd41ku7ifo58q7ry1spgk13qk7duxr8l4/amazing_grace.pdf",
            False,
            True,
        ),
        Hymn(
            1011,
            "26/ed/26ed09a6097f11efa04beeeeac1ed97cd3b2787d/holding_hands_around_the_world.pdf",
        ),
        Hymn(
            1012,
            "or/lf/orlfd3mf3clkpfto7pdywfxpel9bmidbtpecnu2s/anytime_anywhere.pdf",
            False,
            True,
        ),
        Hymn(
            1013,
            "gi/hi/gihiqq3209ffpau17frji60efsgq61rljixxgos5/gods_gracious_love.pdf",
        ),
        Hymn(
            1014,
            "9v/mn/9vmndz16d9l9h7l2zr3wtp122ypr5i8yjy427s13/my_shepherd_will_supply_my_need.pdf",
        ),
        Hymn(
            1015,
            "hp/xf/hpxfkr5dzxbw92hwj9vqsduwh0sbo150jetjdx50/oh_the_deep_deep_love_of_jesus.pdf",
            False,
            True,
        ),
        Hymn(
            1016,
            "a6/ux/a6uxtghps14i4ssoozcejgs9cibasyq6odo6pdxr/behold_the_wounds_in_jesus_hands.pdf",
        ),
        Hymn(
            1017,
            "7q/zp/7qzpq1vulnt4n4l9arsex718dezssq7bw8obd1bc/this_is_the_christ.pdf",
        ),
        Hymn(
            1018, "mm/vi/mmvisbiiw57dvknkaeb8n0qwo2fftbv5sfnvwxtp/come_lord_jesus.pdf"
        ),
        Hymn(
            1019,
            "g6/1i/g61im34xzkp4g57lkpulstl8s13ia5d3z837t8mp/to_love_like_thee.pdf",
            False,
            True,
        ),
        Hymn(
            1020,
            "gp/9w/gp9wrc3mo329pfa8awa8rmend5zil6tstukclxls/softly_and_tenderly_jesus_is_calling.pdf",
        ),
        Hymn(
            1021,
            "8q/wa/8qwassgx63hy67boll7v4e52ro459q4d0lzxvs2w/i_cant_count_them_all.pdf",
        ),
        Hymn(
            1022,
            "yi/jw/yijwjtstvopci0avkh4ol8l823nobcqptlfcxvn9/faith_in_every_footstep.pdf",
        ),
        Hymn(
            1023,
            "lv/8d/lv8dpnyjrmynmua154j1fvkv7f1n9a2ykizdmk8b/standing_on_the_promises.pdf",
        ),
        Hymn(
            1024,
            "8o/d6/8od657vpjqxyhzjiv95vjr5ixxdqfycxzdmozezi/i_have_faith_in_the_lord_jesus_christ.pdf",
        ),
        Hymn(
            1025,
            "jc/kp/jckptf6savvxab34ny5dbcv2236h3g1gld5vt09r/take_my_heart_and_let_it_be_consecrated.pdf",
        ),
        Hymn(
            1026,
            "nu/81/nu81fvjq9ab9f2d9t8i1owhqpgm60tq1343inec7/holy_places.pdf",
            False,
        ),
        Hymn(1027, "05/s0/05s0daaceszp9yp01jmthqmuamg9231u7o3mih2q/welcome_home.pdf"),
        Hymn(
            1028,
            "uk/lw/uklwlgmummoix6b65m2301gh0ylcmpz6j43b0swo/this_little_light_of_mine.pdf",
        ),
        Hymn(
            1029,
            "7n/6i/7n6irgk6xct34xz18hf8xtu27wmzbnce48gs2ljb/i_cant_count_them_all.pdf",
            False,
        ),
        Hymn(
            1030,
            "yn/ge/yngevzb1vct2puwrd4bmvreo3jfdeidixqu2293v/close_as_a_quiet_prayer.pdf",
        ),
        Hymn(
            1031,
            "pt/z7/ptz77oj92sut1n1rp20cyu0fl11z8ffvwxd42lwi/come_hear_the_word_the_lord_has_spoken.pdf",
        ),
        Hymn(
            1032,
            "bw/97/bw97csg5z49rszwumth3j462wogedt05yzs7ez6d/look_unto_christ.pdf",
            False,
        ),
        Hymn(
            1033,
            "oc/5f/oc5ftg2dhfvlbidqesh2ty60hclepf5h9zu0alak/oh_how_great_is_our_joy.pdf",
        ),
        Hymn(
            1034, "u9/iw/u9iwsqur10qc7fhwsxz2cyzq6tjfpqch4i21vqrv/im_a_pioneer_too.pdf"
        ),
        Hymn(
            1035,
            "m5/s0/m5s0ktzhzxk1bowxoxghrejmifmob0y0s9za6e7e/as_i_keep_the_sabbath_day.pdf",
            False,
        ),
        Hymn(
            1036,
            "3n/fl/3nfl2q53dbl7kibtafna1prq4n4q3s382lysumn0/read_the_book_of_mormon_and_pray.pdf",
        ),
        Hymn(
            1037,
            "5l/80/5l805n6sfgwtztrm5vwve0t7zto3yjrwu2zt2nuw/im_gonna_live_so_god_can_use_me.pdf",
        ),
        Hymn(
            1038,
            "u7/99/u799ddbgvv07qt91kwtzalapm05d2w83sl7gcg8t/the_lords_my_shepherd.pdf",
            False,
        ),
        Hymn(1039, "of/s1/ofs1rwmz213u27haebciuvazv33uyfpfdul4vwgr/because.pdf"),
        Hymn(
            1040,
            "l2/kx/l2kxmn57mbwszynpge3qqqx9u3ex1o0atabmc9sa/his_voice_as_the_sound.pdf",
        ),
        Hymn(
            1041,
            "b1/xl/b1xltz3yvbcavk7rkh8sbbbjtdoghe69dbn4f59q/o_lord_who_gave_thy_life_for_me.pdf",
        ),
        Hymn(
            1201,
            "24/78/2478120a097f11efae13eeeeac1e705949a29d62/hail_the_day_that_sees_him_rise.pdf",
            False,
        ),
        Hymn(
            1202,
            "80/04/800459b10e8611efa950eeeeac1ef0d0090f76f2/he_is_born_the_divine_christ_child.pdf",
            False,
            True,
            offsets=dict(letter=(0.82, 0.137)),
        ),
        Hymn(
            1203,
            "2a/d4/2ad4f232097f11efabb0eeeeac1e06f99913c180/what_child_is_this.pdf",
        ),
        Hymn(1204, "29/45/29450364097f11efb9ceeeeeac1ed262191adfc5/star_bright.pdf"),
        Hymn(
            1205,
            "d8/4o/d84ogspp8cp0nnzfe9n6cmsjscziveuxvtfb40bt/let_easter_anthems_ring.pdf",
            False,
            True,
        ),
        Hymn(1206, "9a/90/9a9067jxwg1y0rkf58wzwvqhkax8oyrh2xvbgzmf/were_you_there.pdf"),
        Hymn(
            1207,
            "fj/ls/fjlswc2uz90wk7tldnzp44ek65sttr1vl73qbcur/still_still_still.pdf",
            False,
            True,
        ),
    ],
    title="Cantiques \x96 Pour le foyer et l\x92église",
    t_font_size=dict(a4=33, letter=34),
    hymn_link_text="Scannez ce code pour accéder à ces hymnes numériquement",
    rev_text="Révision",
    lang="fra",
)


# noinspection SpellCheckingInspection
por = DocData(
    [
        Hymn(
            1001,
            "0e/a8/0ea81285073d11efae2feeeeac1ed46377082433/come_thou_fount_of_every_blessing.pdf",
            False,
        ),
        Hymn(
            1002,
            "59/cb/59cb4e5e0cb311ef8f10eeeeac1ecb45755560c4/when_the_savior_comes_again.pdf",
        ),
        Hymn(
            1003,
            "4b/61/4b6145ea0cb311ef9f33eeeeac1efd649a526215/it_is_well_with_my_soul.pdf",
        ),
        Hymn(
            1004,
            "4a/c5/4ac505df0cb311ef88feeeeeac1e90d53b8b981f/i_will_walk_with_jesus.pdf",
        ),
        Hymn(
            1005,
            "48/01/4801ee500cb311efac02eeeeac1e2d1ab1d37dfb/his_eye_is_on_the_sparrow.pdf",
        ),
        Hymn(
            1006,
            "57/6e/576e247b0cb311ef9f33eeeeac1efd64e11347d2/think_a_sacred_song.pdf",
        ),
        Hymn(
            1007,
            "42/d7/42d79aad0cb311ef9be7eeeeac1ec3fd988b6e0b/as_bread_is_broken.pdf",
            False,
        ),
        Hymn(
            1008,
            "43/c7/43c778ea0cb311ef8f34eeeeac1ec1d405de0b25/bread_of_life_living_water.pdf",
            False,
            True,
        ),
        Hymn(1009, "44/95/449550400cb311ef81e1eeeeac1e92868734b100/gethsemane.pdf"),
        Hymn(
            1010,
            "ab/1v/ab1v5rnkdvaxzy1w0uo52lmdet22ldz674vdv1vz/amazing_grace.pdf",
            False,
            True,
        ),
        Hymn(
            1011,
            "4a/14/4a14a1ae0cb311ef9be7eeeeac1ec3fda2cf4ae2/holding_hands_around_the_world.pdf",
        ),
        Hymn(
            1012,
            "rq/qe/rqqe9n9jrk2y1d9fsruysik42jc4yqss0c9q2dvx/anytime_anywhere.pdf",
            False,
            True,
        ),
        Hymn(
            1013,
            "1o/nb/1onbjq054l153fjyrjqyv4wtedufo8fer4jhcfjx/gods_gracious_love.pdf",
        ),
        Hymn(
            1014,
            "d8/3e/d83e581j0kf5j02w8sz57hj2xudi01ety1j9weo4/my_shepherd_will_supply_my_need.pdf",
        ),
        Hymn(
            1015,
            "9l/lh/9llhcchcn6zsovzsfzy33m7wt4ss037n2lzynier/oh_the_deep_deep_love_of_jesus.pdf",
            False,
            True,
        ),
        Hymn(
            1016,
            "ls/xu/lsxudhhk6p5wfb1ofau1g6qoqss767nhscp0r0vt/behold_the_wounds_in_jesus_hands.pdf",
        ),
        Hymn(
            1017,
            "tx/ts/txtsjdh2lf3rz110np604r2b6wza73nyrdbgy4u2/this_is_the_christ.pdf",
        ),
        Hymn(
            1018, "29/ht/29htr2piqnd2gn5bdjovd30y5gwhs8pemkz7cbjb/come_lord_jesus.pdf"
        ),
        Hymn(
            1019,
            "5r/6h/5r6hc4i2m83hs7lomd7gb5cpbn5bjkvsq3qxu76p/to_love_like_thee.pdf",
            False,
            True,
        ),
        Hymn(
            1020,
            "vb/dk/vbdk330ilbuhc7179mzab5llhkuentinm1y5qryt/softly_and_tenderly_jesus_is_calling.pdf",
        ),
        Hymn(
            1021,
            "ec/f8/ecf8sg80uyj49r5d846lmcm8dyf9bqqhu3y84sd4/i_know_that_my_savior_loves_me.pdf",
        ),
        Hymn(
            1022,
            "2z/4z/2z4ztwzyh4782ouq2v9d5dhi16gagp2czt0r7fas/faith_in_every_footstep.pdf",
        ),
        Hymn(
            1023,
            "sv/mn/svmnn3qv1rhgymfbc8sj1pmrv86lfngwurgrmyfo/standing_on_the_promises.pdf",
        ),
        Hymn(
            1024,
            "xr/i1/xri1fqdf6xw1qx3povhuwcwrkr9fx8prpl338oux/i_have_faith_in_the_lord_jesus_christ.pdf",
        ),
        Hymn(
            1025,
            "vr/b0/vrb0rvx60ru6lrtyu6eslhah7hfjj1o3qks2xus1/take_my_heart_and_let_it_be_consecrated.pdf",
        ),
        Hymn(
            1026,
            "3n/1y/3n1yi7fmpimb199y2k3o3vnxdaxw6q4xd9t3g09p/holy_places.pdf",
            False,
        ),
        Hymn(1027, "lg/v1/lgv153h44t36jrvtn6aewq5ti5nzo4apdv0nm2k8/welcome_home.pdf"),
        Hymn(
            1028,
            "3d/4v/3d4v9nqdsc7es9aigcx0uu4cbam4ekiriljnebk1/this_little_light_of_mine.pdf",
        ),
        Hymn(
            1029,
            "fg/5f/fg5ffnv5hcbt9ed2a536ufs2rebkl49xr6xx55og/i_cant_count_them_all.pdf",
            False,
        ),
        Hymn(
            1030,
            "7n/lx/7nlxw0awrwm48t3rm9zy44i92h6ve50ovhboyk56/close_as_a_quiet_prayer.pdf",
        ),
        Hymn(
            1031,
            "lz/0h/lz0hcxwj4zmix2r5nl17trs1knzrfkqcosi31cw4/come_hear_the_word_the_lord_has_spoken.pdf",
        ),
        Hymn(
            1032,
            "ve/kq/vekq8lhs33l7aj83wuugsy0x5n2snn7l3u5c8wp8/look_unto_christ.pdf",
            False,
        ),
        Hymn(
            1033,
            "vi/kv/vikvr874exjzrx3iaxvm0ba0m606hzjc7z8wdf4n/oh_how_great_is_our_joy.pdf",
        ),
        Hymn(
            1034, "69/n3/69n3vkkfo72ydsap47zuz03kfbj3nywklo6lxlet/im_a_pioneer_too.pdf"
        ),
        Hymn(
            1035,
            "9b/2v/9b2vc5ztzcowrt40ph214h2kz72xbxvgmc8swsni/as_i_keep_the_sabbath_day.pdf",
            False,
        ),
        Hymn(
            1036,
            "ln/pl/lnplx328sxrw2d4e2veap39i8wvjvstl0d47z4ja/read_the_book_of_mormon_and_pray.pdf",
        ),
        Hymn(
            1037,
            "rk/cw/rkcwxikjn02egjq6ji50xs8wv31dijkxw2myblk7/im_gonna_live_so_god_can_use_me.pdf",
        ),
        Hymn(
            1038,
            "vf/p1/vfp1t5yawhhqknr3ewykddhvzn44q3fbz96bdpxo/the_lords_my_shepherd.pdf",
            False,
        ),
        Hymn(1039, "18/xf/18xf2nv5nl53umpxu6mxtfuhob4pyxgdbw5n48r9/because.pdf"),
        Hymn(
            1040,
            "q5/ft/q5ft2in03jylm6szyeuhksi7irnbs77bq84bkz0j/his_voice_as_the_sound.pdf",
        ),
        Hymn(
            1041,
            "8h/7j/8h7jwm8q2be68hfhxbay979cheh8hps1wcapkacc/o_lord_who_gave_thy_life_for_me.pdf",
        ),
        Hymn(
            1201,
            "45/87/458703350cb311efaf07eeeeac1e99beb8fedf6e/hail_the_day_that_sees_him_rise.pdf",
            False,
        ),
        Hymn(
            1202,
            "46/a4/46a45a200cb311ef8a83eeeeac1e9d163846f078/he_is_born_the_divine_christ_child.pdf",
            False,
            True,
        ),
        Hymn(
            1203,
            "58/9f/589fedbe0cb311efb8f9eeeeac1e6f4bd4ca924c/what_child_is_this.pdf",
        ),
        Hymn(1204, "56/47/564730a20cb311efa648eeeeac1e2f595efab152/star_bright.pdf"),
        Hymn(
            1205,
            "68/82/6882hfxekci93yiwfarg91fgkg1tgzukh2x0kwjx/let_easter_anthems_ring.pdf",
            False,
            True,
        ),
        Hymn(1206, "s9/ru/s9ru99vxqws6c6nxrvueojhgstv6jnzekdolfe50/were_you_there.pdf"),
        Hymn(
            1207,
            "ue/ih/ueihr5b8g7df8p38iju29vs5qky39wsnc0dvigeo/still_still_still.pdf",
            False,
            True,
        ),
    ],
    title="Hinos \x97 Para o Lar e para a Igreja",
    t_font_size=dict(a4=34, letter=35),
    hymn_link_text="Digitalize este código para acessar esses hinos digitalmente",
    rev_text="Revisão",
    lang="por",
)


# noinspection SpellCheckingInspection
spa = DocData(
    [
        Hymn(
            1001,
            "c2/84/c284c254073b11efbfd2eeeeac1e0cc7c94404a1/come_thou_fount_of_every_blessing.pdf",
            False,
        ),
        Hymn(
            1002,
            "6b/9b/6b9b7f4b0ca311ef8fc9eeeeac1e0de2bbf1578f/when_the_savior_comes_again.pdf",
        ),
        Hymn(
            1003,
            "61/2d/612daab80ca311ef9be7eeeeac1ec3fd60ec888c/it_is_well_with_my_soul.pdf",
        ),
        Hymn(
            1004,
            "60/96/609625ac0ca311efa648eeeeac1e2f5955fd268c/i_will_walk_with_jesus.pdf",
        ),
        Hymn(
            1005,
            "5e/a3/5ea3565f0ca311efb941eeeeac1ef7cfdf0191ba/his_eye_is_on_the_sparrow.pdf",
        ),
        Hymn(
            1006,
            "69/dc/69dcdf5b0ca311ef8e16eeeeac1ea134e1752487/think_a_sacred_song.pdf",
        ),
        Hymn(
            1007,
            "5a/54/5a546e9b0ca311ef80a4eeeeac1e1a8976dcfe6c/as_bread_is_broken.pdf",
            False,
        ),
        Hymn(
            1008,
            "5b/4c/5b4c8a3f0ca311efaf3ceeeeac1e008b2ff6cee6/bread_of_life_living_water.pdf",
            False,
            True,
        ),
        Hymn(1009, "5c/2a/5c2ab53a0ca311ef8fc9eeeeac1e0de2710d4e06/gethsemane.pdf"),
        Hymn(
            1010,
            "rj/md/rjmdkfwcvyj40z9x5mptv3rlp3mjq0r3f2ajvz3o/amazing_grace.pdf",
            False,
            True,
        ),
        Hymn(
            1011,
            "5f/cd/5fcd576f0ca311efb82eeeeeac1e03e733245bc0/holding_hands_around_the_world.pdf",
        ),
        Hymn(
            1012,
            "ie/jk/iejkdwj6ogfhn6gcok301zck7s0vgbe1ch5ltiqa/anytime_anywhere.pdf",
            False,
            True,
        ),
        Hymn(
            1013,
            "zu/nl/zunlwr8mxkcfs1kgwcupi3y2kyhds082vokow4e3/gods_gracious_love.pdf",
        ),
        Hymn(
            1014,
            "w1/z8/w1z84shlyiaxdiv3dz98f2otmp1h8g11qxiaooxl/my_shepherd_will_supply_my_need.pdf",
        ),
        Hymn(
            1015,
            "27/fo/27fo18n3uiobq291iegxy2j3j96rqc73g5mmavfb/oh_the_deep_deep_love_of_jesus.pdf",
            False,
            True,
        ),
        Hymn(
            1016,
            "1d/cb/1dcbgah3w40qzk0yj2mw2mqbi9mxjohrzo0t9z1r/behold_the_wounds_in_jesus_hands.pdf",
        ),
        Hymn(
            1017,
            "k1/r6/k1r6w3qrec4frhpd9uv7xqst2ds3qqihw2k2ebwe/this_is_the_christ.pdf",
        ),
        Hymn(
            1018, "af/6a/af6acu0yilofg8ir3okj65ok0dzgj4pztjbz9rvt/come_lord_jesus.pdf"
        ),
        Hymn(
            1019,
            "v9/3m/v93moe9wq88u72jcegrml14tiay33yhelzi1u14c/to_love_like_thee.pdf",
            False,
            True,
        ),
        Hymn(
            1020,
            "dd/lr/ddlron658e7ddvysueq896d705ocaiegkyctm79l/softly_and_tenderly_jesus_is_calling.pdf",
        ),
        Hymn(
            1021,
            "qq/z5/qqz5xu4ml313y9y5zc9ddrtjh2v0dy4p0a7oetcm/i_cant_count_them_all.pdf",
        ),
        Hymn(
            1022,
            "nf/y0/nfy0b6o8a8nict43hjiw8wouzhygzq1j8n0r0xb9/faith_in_every_footstep.pdf",
        ),
        Hymn(
            1023,
            "od/gb/odgbnqo5s3xtpj1gfuj4o0cexj494dznmynhzroz/standing_on_the_promises.pdf",
        ),
        Hymn(
            1024,
            "7a/5j/7a5josf3w4uqvia5kid7d25e7qbi41h48bg2va4b/i_have_faith_in_the_lord_jesus_christ.pdf",
        ),
        Hymn(
            1025,
            "m4/hx/m4hxp2k110signsnn2og7nuvlzitpqsf56oujb8k/take_my_heart_and_let_it_be_consecrated.pdf",
        ),
        Hymn(
            1026,
            "m4/t2/m4t2kz3s1cm4qirncmy6c5u99v27hm6sysib5y5g/holy_places.pdf",
            False,
        ),
        Hymn(1027, "2f/03/2f0382g3csuryqk8ed6fyc7eyav2m14hig9475t1/welcome_home.pdf"),
        Hymn(
            1028,
            "5y/hb/5yhb3bx04vzoib9knwtkwrqlkgutxvphb6e6wo4c/this_little_light_of_mine.pdf",
        ),
        Hymn(
            1029,
            "td/3c/td3crppjmqvown4gld4jt294zy5u7sg01i79su78/i_cant_count_them_all.pdf",
            False,
        ),
        Hymn(
            1030,
            "1s/dw/1sdw6aog5dz1o7bdcsd8ymtd5gfldd433ha552e3/close_as_a_quiet_prayer.pdf",
        ),
        Hymn(
            1031,
            "dd/hx/ddhx8cggoprf726m2fro8xfj7l97fzqsyv9df4w8/come_hear_the_word_the_lord_has_spoken.pdf",
        ),
        Hymn(
            1032,
            "xr/5w/xr5wt8srqghwh8fdipaqw9fogxykygfk36aj12fx/look_unto_christ.pdf",
            False,
        ),
        Hymn(
            1033,
            "9z/54/9z54zv645djbm8uc88fz436fztc9unecxlq5f01u/oh_how_great_is_our_joy.pdf",
        ),
        Hymn(
            1034, "bu/6s/bu6spilnlhr3srp430n3pwzjene7zomnqhaveenw/im_a_pioneer_too.pdf"
        ),
        Hymn(
            1035,
            "2z/yc/2zyc0ve956dpyokbyo9ft460oynapd2ft1po395n/as_i_keep_the_sabbath_day.pdf",
            False,
        ),
        Hymn(
            1036,
            "5g/0c/5g0c09k3vi05akrwfcp9ekeficqo44pisoktzrf1/read_the_book_of_mormon_and_pray.pdf",
        ),
        Hymn(
            1037,
            "gb/92/gb92hl3y9zfgbw5m28vofy9ht2jtdsz3qrd7zv09/im_gonna_live_so_god_can_use_me.pdf",
        ),
        Hymn(
            1038,
            "wg/68/wg68cd6nirfbhchkq1j0tjb49kjg96s3k9vdrwa8/the_lords_my_shepherd.pdf",
            False,
        ),
        Hymn(1039, "aq/i0/aqi0oy1939ymjl1skxy7zd0orf9x9chhe8dwlpb0/because.pdf"),
        Hymn(
            1040,
            "kk/k8/kkk89410m2osdpeoqpby7px2ra8lovnzj1qcy41o/his_voice_as_the_sound.pdf",
        ),
        Hymn(
            1041,
            "o1/sb/o1sb39bgi537vs0d895qnvncobt7pxwp5nmfl5yc/o_lord_who_gave_thy_life_for_me.pdf",
        ),
        Hymn(
            1201,
            "5d/1e/5d1e15ee0ca311efb82eeeeeac1e03e79b85b9b2/hail_the_day_that_sees_him_rise.pdf",
            False,
        ),
        Hymn(
            1202,
            "5d/ba/5dbacb230ca311ef823ceeeeac1ea7cf84767a94/he_is_born_the_divine_christ_child.pdf",
            False,
            True,
        ),
        Hymn(
            1203,
            "6a/de/6ade49c60ca311ef89fbeeeeac1e28fb7942f974/what_child_is_this.pdf",
        ),
        Hymn(1204, "80/02/8002fa220e8611efb3baeeeeac1e55fa95392dc5/star_bright.pdf"),
        Hymn(
            1205,
            "ac/au/acauj22rj8p1prejn4zq4w5v00x0ygkk9mzk47rx/let_easter_anthems_ring.pdf",
            False,
            True,
        ),
        Hymn(1206, "v3/gd/v3gd4rag00g44u16ik7v8noshtwt94gq6uc2law8/were_you_there.pdf"),
        Hymn(
            1207,
            "a2/yr/a2yr0k9yk46j787x26u6wlz5kaxr04u05idcyvwh/still_still_still.pdf",
            False,
            True,
        ),
    ],
    title="Himnos \x97 Para el hogar y la Iglesia",
    t_font_size=dict(a4=33, letter=33),
    hymn_link_text="Escanee este código para acceder los himnos digitalmente",
    rev_text="Revisión",
    lang="spa",
)


lang_map: dict[str, DocData] = {
    "eng": eng,
    "fra": fra,
    "por": por,
    "spa": spa,
}
