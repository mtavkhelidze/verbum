from typing import List, Tuple

import numpy as np
import scipy
from flask import Flask
from nltk import sent_tokenize
from sentence_transformers import SentenceTransformer

from app.fp import Option, Some, nil


class NLP:
    model = None
    app: Flask = None

    def __init__(self, app: Flask):
        self.app = app
        with app.app_context():
            self.model = SentenceTransformer("./model.bin")

    def make_embeddings(self, sentences: List[str]) -> List[Tuple[str, np.ndarray]]:
        embeds = self.model.encode(sentences)
        return list(zip(sentences, embeds))

    @staticmethod
    def sentences(text: str) -> Option[List[str]]:
        xs = sent_tokenize(text)
        return Some(xs) if len(xs) > 0 else nil

    @staticmethod
    def similar_sentence_ids(sent: np.ndarray, sentences: List[np.ndarray]):
        distances = scipy.spatial.distance.cdist([sent], sentences, "cosine")[0]
        results = zip(range(1, len(distances) + 1), distances)
        return sorted(results, key=lambda x: x[1])[0:6]
