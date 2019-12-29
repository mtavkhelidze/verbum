import textwrap


def shorten(text: str, to: int = 80) -> str:
    return textwrap.shorten(text, to)
