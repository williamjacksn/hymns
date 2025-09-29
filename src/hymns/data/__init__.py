from .base import DocData
from .eng import eng
from .fra import fra
from .por import por
from .spa import spa

lang_map: dict[str, DocData] = {
    "eng": eng,
    "fra": fra,
    "por": por,
    "spa": spa,
}
