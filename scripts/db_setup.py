import os
from sqlite3 import connect

import logging
from nltk import sent_tokenize

log = logging.getLogger("db-setup")
logging.basicConfig(level=logging.INFO)

snippet_01 = os.path.join(os.path.dirname(__file__), "snippet-01.txt")
snippet_02 = os.path.join(os.path.dirname(__file__), "snippet-02.txt")

sentences = []

with open(snippet_01, "r", encoding="utf-8") as fd:
    log.info(f"Reading {snippet_01}")
    text = fd.read()
    sentences.append(sent_tokenize(text=text, language="english"))

with open(snippet_02, "r", encoding="utf-8") as fd:
    log.info(f"Reading {snippet_02}")
    text = fd.read()
    sentences.append(sent_tokenize(text=text, language="english"))

con = connect("./data/verbum.sqlite3")

snippets_sql = """
    create table snippets (
        id integer primary key autoincrement,
        count int not null,
        tag_line text not null
    )
"""

log.info(f"Create table snippets")
con.execute(snippets_sql)

sentences_sql = """
    create table sentences (
        id integer primary key autoincrement,
        snippet_id integer,
        body text not null
    )
"""

log.info(f"Create table sentences")
con.execute(sentences_sql)

log.info(f"Populate tables with data")
for i, s in enumerate(sentences):
    con.execute(
            """insert into snippets(id, count, tag_line) values(?, ?, ?)""",
            (i + 1, len(s), s[0],)
            )

    for sent in s:
        q = f"insert into sentences(snippet_id, body) values(?, ?)"
        con.execute(q, (i + 1, sent))

con.commit()
con.close()
