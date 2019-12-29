from sqlite3 import Row, connect
from typing import List, Optional

from flask import g

from constants import DB_NAME
from data_model import (
    Sentence,
    Snippet,
    SnippetWithSentences,
    make_full_snippet,
    make_sentence,
    make_snippet,
    )


def db_get():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect(DB_NAME)
        db.row_factory = Row
    return db


def db_query(query, args=(), one=False) -> List[Row]:
    cur = db_get().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def db_get_all_snippets() -> List[Snippet]:
    rows = db_query("select * from snippets")
    return list(map(make_snippet, rows))


def db_get_snippet_for(idx: int) -> Optional[SnippetWithSentences]:
    rows = db_query(
            "select st.* from snippets as sn, sentences as st where sn.id = st.snippet_id and "
            "sn.id = ?",
            (idx,)
            )
    if len(rows) > 0:
        return make_full_snippet(rows)
    return None


def db_get_sentence_for(idx: int) -> Sentence:
    rows = db_query("select * from sentences where id = ?", (idx,))
    return make_sentence(rows[0])


def db_get_sentences_with(ids: List[int]) -> Optional[List[Sentence]]:
    rows = db_query(
            "select * from sentences where id in ("
            + ",".join(map(str, ids))
            + ")"
            )
    if len(rows) < 1:
        return None
    return list(map(make_sentence, rows))


def db_create_snippet(sents: List[str]) -> int:
    if len(sents) < 1:
        return 0
    con = db_get()
    cur = con.execute("insert into snippets (count, tag_line) values(?, ?)", (len(sents), sents[0],))
    rowid = cur.lastrowid
    vals = ((rowid, body) for body in sents)
    cur.executemany(f"insert into sentences (snippet_id, body) values(?, ?)", vals)
    cur.close()
    con.commit()
    return rowid
