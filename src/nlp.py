from typing import List

import numpy as np
import scipy
import sys
from nltk import sent_tokenize
from sentence_transformers import SentenceTransformer

from database_utils import db_query


this = sys.modules[__name__]

model = SentenceTransformer('bert-base-nli-mean-tokens')

_embeds: List[np.ndarray] = []


def init_nlp():
    rows = db_query("select * from sentences")
    update_embeddings([r["body"] for r in rows])


def split_into_sentences(text: str) -> List[str]:
    return sent_tokenize(text=text, language="english")


def update_embeddings(sents: List[str]):
    embeds = model.encode(sents)
    _embeds.extend(embeds)


def similar_sentence_ids(sent: str):
    query_embedding = model.encode([sent])
    distances = scipy.spatial.distance.cdist(query_embedding, _embeds, "cosine")[0]
    results = zip(range(len(distances)), distances)
    return sorted(results, key=lambda x: x[1])[0:6]
