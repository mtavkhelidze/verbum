from typing import Callable, List, TypeVar


T = TypeVar("T")
R = TypeVar("R")

MapFunction = Callable[[T], R]


class Seq(List[T]):
    def __init__(self, *args):
        super(Seq, self).__init__(args)

    def map(self, fn: MapFunction) -> "Seq[R]":
        return Seq(*[fn(x) for x in self])
