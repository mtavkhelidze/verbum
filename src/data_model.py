from sqlite3 import Row
from typing import List, Tuple

from typing_extensions import TypedDict

from utilities import shorten


class Sentence(TypedDict):
    id: int
    body: str


class SimilarSentence(Sentence):
    score: float


class Snippet(TypedDict):
    id: int
    count: int
    tagLine: str


class SnippetWithSentences(Snippet):
    parts: List[Sentence]


def make_snippet(row: Row) -> Snippet:
    return Snippet(
            id=row["id"],
            count=row["count"],
            tagLine=shorten(row["tag_line"])
            )


def make_sentence(row: Row) -> Sentence:
    return Sentence(
            id=row["id"],
            body=row["body"]
            )


def make_full_snippet(rows: List[Row]) -> SnippetWithSentences:
    parts = list(map(make_sentence, rows))
    return SnippetWithSentences(
            id=rows[0]["id"],
            count=len(rows),
            tagLine=shorten(rows[0]["body"]),
            parts=parts
            )


def make_similar_sentence(ws: Tuple[int, float], s: Sentence) -> SimilarSentence:
    return SimilarSentence(
            id=s["id"],
            body=s["body"],
            score=ws[1]
            )
