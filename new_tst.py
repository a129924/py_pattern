from typing import Type, Tuple, Any


class AnyTypeVariable:
    def __new__(cls, arg=...) -> "AnyTypeVariable":
        instance = super().__new__(cls)
        instance.arg = arg
        return instance

    def __init__(self, arg=...) -> None:
        self.arg = arg

    # def __setitem__(self, key, value):
    #     self.arg = value
    #     print(self.arg)

    def __str__(self) -> str:
        return f"{self.arg}"


def is_iterable_not_str(obj: Type) -> bool:
    from collections.abc import Iterable

    return isinstance(obj, Iterable) and not isinstance(obj, str)


any_value1 = AnyTypeVariable()
any_value2 = AnyTypeVariable()
any_value3 = AnyTypeVariable()

# print(any_value.arg)

structure: Tuple[Tuple[AnyTypeVariable, Any], ...] = (
    (any_value1, 1),
    (any_value2, 2),
    (any_value3, 3),
)


for s in structure:
    s[0].arg = s[1]


print(any_value1)
print(any_value2)
print(any_value3)
