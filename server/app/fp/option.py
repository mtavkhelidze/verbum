from typing import Callable, Generic, Optional, TypeVar


# Shamelessly stolen from http://bit.ly/369lS2Z with a slight modifications

A = TypeVar("A")
B = TypeVar("B")


class Monad(Generic[A]):
    defined: bool = False
    value: Optional[A] = None

    # pure :: a -> M a
    @staticmethod
    def pure(x: A) -> "Monad[A]":
        raise Exception("pure method needs to be implemented")

    # flat_map :: # M a -> (a -> M b) -> M b
    def flat_map(self, f: Callable[[A, "Monad[B]"], "Monad[B]"]) -> "Monad[B]":
        raise Exception("flat_map method needs to be implemented")

    # getOrElse :: # M a -> a -> a
    def get_or_else(self, alt: B) -> A:
        raise Exception("get_or_else method needs to be implemented")

    # map :: # M a -> (a -> b) -> M b
    def map(self, f: Callable[[A], B]) -> "Monad[B]":
        return self.flat_map(lambda x: self.pure(f(x)))


class Option(Monad[A]):
    # pure :: a -> Option a
    @staticmethod
    def pure(x: A) -> "Option[A]":
        return Some(x)

    # flat_map :: # Option a -> (a -> Option b) -> Option b
    def flat_map(self, f: Callable[[A], "Option[B]"]) -> "Option[B]":
        if self.defined:
            return f(self.value)
        else:
            return nil


class Some(Option):
    def __init__(self, value: A):
        self.value = value
        self.defined = True

    def get_or_else(self, _: B) -> A:
        return self.value


class Nil(Option):
    def __init__(self):
        self.value = None
        self.defined = False

    def get_or_else(self, alt: B) -> B:
        return alt


nil = Nil()
