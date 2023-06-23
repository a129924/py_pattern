from .base import BaseAnyElement, BaseManyElement, BaseOrMather
from typing import Any


class AnyElement(BaseAnyElement):
    def __new__(cls, arg: Any = ...) -> "AnyElement":
        instance = super().__new__(cls)
        instance.arg = arg

        return instance

    def __init__(self, arg: Any = ...) -> None:
        self.arg = arg

    def __eq__(self, other):
        return True


class ManyElement(BaseManyElement):
    def __eq__(self, other):
        return True


class OrMatcher(BaseOrMather):
    def __init__(self, *iter) -> None:
        self.iter = iter

    def __or__(self, other) -> bool:
        return other in self.iter
