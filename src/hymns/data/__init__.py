from . import eng, fra, por, spa
from .base import DocData

lang_map: dict[str, DocData] = {
    "eng": eng.doc_data,
    "fra": fra.doc_data,
    "por": por.doc_data,
    "spa": spa.doc_data,
}
