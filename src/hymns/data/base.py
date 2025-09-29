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
