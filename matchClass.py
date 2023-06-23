from typing import Type, Any, Callable, overload


class MatchError(Exception):
    pass


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

    def otherwise(self):
        # 如果沒匹配到 會觸發預設的回傳值
        ...


name = "A123A"
my_match = Match(20)

# fmt: off
my_match.case(lambda x:x < 1, f"我是{name}")\
        .case(lambda x: 10 > x > 1, "我是20")\
        .case(lambda x: x == 20 , f"我是{name}-1")

# my_match.case(lambda x: x > 1)
# fmt: on


print(my_match.get_value_if_match)
# print(isinstance(lambda x: x, type))
# def process_data(data, operation):
#     return operation(data)


# print(process_data(3, lambda x: 4 > x > 1))

tst = lambda x, *others: print(f"Got 1 and a nested sequence: x={x}, other={others}")


@overload
def case(match_param: Any, if_match_return_value: Any) -> Any:
    ...


@overload
def case(match_param: Any, other_param: Any, if_match_return_value: Any) -> Any:
    ...


def case(match_param, *args):
    print(match_param, args)


case(1, [2, 3, 4])
