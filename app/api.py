from typing import Tuple

from flask import Blueprint, jsonify, request

from . import nlp
from .database import (
    db_get_sentence,
    db_get_sentences_with,
    db_get_snippet,
    db_insert_snippet,
    db_list_sentences,
    db_list_snippets,
    )
from .fp import nil
from .model import ErrorResponse, PostSnippetResponse
from .nlp import NLP


api = Blueprint("api_route", __name__)


def error(message: str) -> Tuple[str, int]:
    return jsonify(ErrorResponse(message=message)), 500


@api.route("/snippet", methods=["POST"])
def post_snippet():
    text = request.json["value"]
    return (NLP.sentences(text)
            .map(nlp.make_embeddings)
            .flat_map(db_insert_snippet)
            .map(lambda sid: PostSnippetResponse(id=sid))
            .map(jsonify)
            .get_or_else(error("Cannot insert snippet."))
            )


@api.route("/snippet/<int:sid>", methods=["GET"])
def get_snippet(sid: int):
    return db_get_snippet(sid).get_or_else(error(f"Cannot get snippet with id {sid}."))


@api.route("/snippet", methods=["GET"])
def list_snippets():
    return jsonify(db_list_snippets())


@api.route("/similar/<int:sid>", methods=["GET"])
def get_similar_sentence(sid: int):
    # todo: de-uglify!
    original = db_get_sentence(sid=sid)
    if original is nil:
        return error(f"Invalid sentence id: {sid}.")

    sentences = db_list_sentences()
    all_embs = list(map(lambda s: s["vector"], sentences))
    sim_ids = NLP.similar_sentence_ids(original.value["vector"], all_embs)
    similar = db_get_sentences_with(sim_ids[1:5])
    original.value["vector"] = None
    return jsonify({
        "original": original.value,
        "similar": similar,
        })
