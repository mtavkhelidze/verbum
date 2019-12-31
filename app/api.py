from typing import Tuple

from flask import Blueprint, jsonify, request

from .db import db_get_snippet, db_insert_snippet, db_list_snippets
from .model import ErrorResponse, PostSnippetResponse
from .nlp import nlp_process_sentences


api = Blueprint("api_route", __name__)


def error(message: str) -> Tuple[str, int]:
    return jsonify(ErrorResponse(message=message)), 500


@api.route("/snippet", methods=["POST"])
def post_snippet():
    text = request.json["text"]
    return (nlp_process_sentences(text)
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
