from typing import List

from nltk import sent_tokenize

from app.fp import Option, Some, nil


def nlp_process_sentences(text: str) -> Option[List[str]]:
    xs = sent_tokenize(text)
    return Some(xs) if len(xs) > 0 else nil
