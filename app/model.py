from typing import List

from typing_extensions import TypedDict

from . import db


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


class Snippet(db.Model):
    __tablename__ = "snippet"

    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(128))

    sentences = db.relationship("Sentence")

    def to_resp(self, with_sentences=True) -> SnippetResponse:
        sentences = [s.to_resp() for s in self.sentences] if with_sentences else None
        return SnippetResponse(
            id=self.id,
            headline=self.headline,
            sentences=sentences,
            count=len(self.sentences)
            )


class Sentence(db.Model):
    __tablename__ = "sentence"

    id = db.Column(db.Integer, primary_key=True)
    snippet_id = db.Column(db.Integer, db.ForeignKey('snippet.id'))
    body = db.Column(db.Text)
    embedding = db.Column(db.LargeBinary)

    @staticmethod
    def create(text: str) -> "Sentence":
        return Sentence(body=text)

    def to_resp(self) -> SentenceResponse:
        return SentenceResponse(
            id=self.id,
            body=self.body,
            score=-1,
            )
