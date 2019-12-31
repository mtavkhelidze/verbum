from typing import List, TypeVar

from app.fp import Option, Some, nil


T = TypeVar("T")


def head(xs: List[T]) -> Option[T]:
    return Some(xs[0]) if len(xs) > 0 else nil
