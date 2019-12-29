import json
import logging as logging

from flask import Flask, abort, g, jsonify, request
from flask_cors import CORS

from constants import APP_NAME
from data_model import make_similar_sentence
from database_utils import (
    db_create_snippet,
    db_get_all_snippets,
    db_get_sentence_for,
    db_get_sentences_with,
    db_get_snippet_for,
    )
from nlp import init_nlp, similar_sentence_ids, split_into_sentences, update_embeddings


logging.basicConfig(format="%(asctime)s : %(name)s : %(message)s", level=logging.INFO)
log = logging.getLogger(APP_NAME)

app = Flask(APP_NAME)
CORS(app)

with app.app_context():
    init_nlp()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/snippets", methods=["GET"])
def get_snippets():
    return jsonify(db_get_all_snippets())


@app.route("/snippets/<int:idx>", methods=["GET"])
def get_snippet(idx: int):
    sn = db_get_snippet_for(idx)
    if sn is not None:
        return jsonify(sn)
    abort(404)


@app.route("/similar/<int:idx>", methods=["GET"])
def post_similar(idx: str):
    sns = db_get_sentence_for(int(idx))
    if sns is None:
        abort(404)
    ids_weights = similar_sentence_ids(sns["body"])
    ids = [i + 1 for i, _ in ids_weights]
    sims = db_get_sentences_with(ids)
    if sims is None:
        abort(404)
    ws = sorted(ids_weights, key=lambda x: x[0])
    similar = [make_similar_sentence(ws[i], s) for i, s in enumerate(sims)]
    res = {
            "original": sns,
            "similar": similar,
            }
    return jsonify(res)


@app.route("/snippets", methods=["POST"])
def post_snippet():
    data = json.loads(request.data)
    sents = split_into_sentences(data.get("value", ""))
    update_embeddings(sents)
    rowid = db_create_snippet(sents)
    return jsonify({"id": rowid})
