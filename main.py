from PyPattern import Match
from PyPattern.Pattern import AnyElement

my_match = Match(20)
any_element = AnyElement()

name = "ABCV"
# fmt: off
my_match.case(lambda x:x < 1, f"我是{name}")\
        .case(lambda x: 10 > x > 1, "我是20")\
        .case(lambda x: x == 20 , f"我是{name}-1")

# my_match.case(lambda x: x > 1)
# fmt: on
print(my_match.get_value_if_match)
print(any_element == 1)
