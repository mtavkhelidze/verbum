from functools import partial
from typing import List, Tuple

import numpy as np

from . import db
from .fp import Option, Some, nil
from .model import Sentence, SentenceDict, SentenceResponse, Snippet, SnippetResponse
from .util import head


def db_insert_snippet(parts: List[Tuple[str, np.ndarray]]) -> Option[int]:
    # todo: de-uglify!
    first = head(parts)
    if first is nil:
        return nil
    headline, _ = first.value
    sentences = map(Sentence.create, parts)
    snippet = Snippet(headline=headline, sentences=list(sentences))
    db.session.add(snippet)
    db.session.flush()
    db.session.commit()
    return Some(snippet.id)


def db_get_snippet(sid: int) -> Option[Snippet]:
    s: Snippet = Snippet.query.get(sid)
    return Some(Snippet.to_resp(s)) if s is not None else nil


def db_list_snippets(limit: int = -1) -> List[SnippetResponse]:
    return list(map(
        lambda s: Snippet.to_resp(s, with_sentences=False),
        Snippet.query.limit(limit).all()
        ))


with_default_score = partial(Sentence.to_dict, -1)


def db_list_sentences() -> List[SentenceDict]:
    sentences = Sentence.query.all()
    return list(map(with_default_score, sentences))


def db_get_sentence(sid: int) -> Option[SentenceDict]:
    sent = Sentence.query.get(sid)
    return Some(with_default_score(sent)) if sent is not None else nil


def db_get_sentences_with(embeds: Tuple[int, float]) -> List[SentenceResponse]:
    ids = {i for i, _ in embeds}
    sents = Sentence.query.filter(Sentence.id.in_(ids)).all()
    result = [Sentence.to_resp(s, embeds[i][1]) for i, s in enumerate(sents)]
    return result
