from typing import List

from . import db
from .fp import Option, Some, nil
from .model import Sentence, Snippet
from .util import head


def db_insert_snippet(parts: List[str]) -> Option[int]:
    # todo: de-uglify!
    headline = head(parts)
    if headline is nil:
        return nil
    sentences = map(Sentence.create, parts)
    snippet = Snippet(headline=headline.value, sentences=list(sentences))
    db.session.add(snippet)
    db.session.flush()
    db.session.commit()
    return Some(snippet.id)


def db_get_snippet(sid: int) -> Option[Snippet]:
    s = Snippet.query.get(sid)
    return Some(s.to_resp()) if s is not None else nil


def db_list_snippets(limit: int = -1) -> List[Snippet]:
    return list(map(
        lambda s: s.to_resp(with_sentences=False),
        Snippet.query.limit(limit).all()
        ))
