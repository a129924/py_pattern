from typing import Any, Callable, Type
from .exceptions import MatchError
from PyPattern.Pattern.base import (
    BaseAnyElement,
    BaseManyElement,
    BaseOrMather,
)  # noqa: F401


class Match:
    def __init__(self, condition: Any) -> None:
        self.condition = condition

    def __getattr__(self, __name: str) -> Any:
        if __name not in dir(self):
            raise MatchError("is not match")

    def case(self, compare_param: Any, get_value_if_match: Any) -> "Match":
        if self.__is_class(compare_param):
            if self.condition == compare_param:
                self.get_value_if_match = get_value_if_match

        elif self.__is_function(compare_param):
            """
            # 支援
            1. lambda x : x == 1
            """
            result = compare_param(self.condition)  # True or False
            if result is True and self.__check_variable_not_in_self():
                self.get_value_if_match = get_value_if_match

        elif compare_param == self.condition and self.__check_variable_not_in_self():
            self.get_value_if_match = get_value_if_match
        return self

    def __is_class(self, obj: Type):
        return isinstance(obj, type)

    def __is_function(self, operation: Callable):
        return callable(operation)

    def __check_variable_not_in_self(self, variable: str = "get_value_if_match"):
        return variable not in dir(self)

    def exhaustive(self):
        # 完整匹配模式 若沒匹配到 會報錯
        ...

    def otherwise(self, default=None):
        # 如果沒匹配到 會觸發預設的回傳值
        ...
        return default

    ###############################################
    def has_type(self, elements, object) -> bool:
        return any(map(lambda element: type(element) == object, elements))

    def find_element_type_position(self, elements: list, object) -> tuple:
        return tuple(
            position
            for position, element in enumerate(elements)
            if type(element) == object
        )

    def match_pairs(self, target: list, pattern: list) -> bool:
        return all(
            map(lambda t, p: t == p or isinstance(p, BaseAnyElement), target, pattern)
        )

    def check_matching_elements(self, target, pattern):
        if len(target) == len(pattern) and not self.has_type(pattern, BaseManyElement):
            return self.match_pairs(target, pattern)

        find_positions = self.find_element_type_position(pattern, BaseManyElement)
        if len(find_positions) == 1:
            return self.match_pairs(
                target, pattern[: find_positions[0]]
            ) and self.match_pairs(target[::-1], pattern[: find_positions[0] : -1])
        else:
            raise ValueError("Too Many type ManyElement")
