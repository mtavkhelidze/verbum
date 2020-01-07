import pickle
from typing import List, Tuple

import numpy as np
from typing_extensions import TypedDict

from app import db


class ErrorResponse(TypedDict):
    message: str


class PostSnippetResponse(TypedDict):
    id: int


class SentenceResponse(TypedDict):
    id: int
    body: str
    score: float


class SnippetResponse(TypedDict):
    id: int
    headline: str
    count: int
    sentences: List[SentenceResponse]


class SentenceDict(SentenceResponse):
    vector: np.ndarray


class Snippet(db.Model):
    __tablename__ = "snippet"

    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(128))

    sentences = db.relationship("Sentence")

    @staticmethod
    def to_resp(s: "Snippet", with_sentences=True) -> SnippetResponse:
        sentences = [Sentence.to_resp(sen) for sen in s.sentences] if with_sentences else None
        return SnippetResponse(
            id=s.id,
            headline=s.headline,
            sentences=sentences,
            count=len(s.sentences)
            )


class Sentence(db.Model):
    __tablename__ = "sentence"

    id = db.Column(db.Integer, primary_key=True)
    snippet_id = db.Column(db.Integer, db.ForeignKey('snippet.id'))
    body = db.Column(db.Text)
    embedding = db.Column(db.PickleType, nullable=False)

    @staticmethod
    def create(data: Tuple[str, np.ndarray]) -> "Sentence":
        body, embedding = data
        return Sentence(body=body, embedding=embedding.dumps())

    @staticmethod
    def to_resp(sentence: "Sentence", score=-1) -> SentenceResponse:
        return SentenceResponse(
            id=sentence.id,
            body=sentence.body,
            score=score,
            )

    @staticmethod
    def to_dict(score: int, sentence: "Sentence") -> SentenceDict:
        return SentenceDict(
            id=sentence.id,
            body=sentence.body,
            score=score,
            vector=pickle.loads(sentence.embedding)
            )
