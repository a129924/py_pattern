class AnyElement:
    def __eq__(self, other):
        return True


class ManyElement:
    def __eq__(self, other):
        return True


class OrMatcher:
    def __init__(self, *iter) -> None:
        self.iter = iter

    def __or__(self, other) -> bool:
        return other in self.iter


many_element = ManyElement()
any_element = AnyElement()


def has_type(elements, object) -> bool:
    return any(map(lambda element: type(element) == object, elements))


def find_element_type_position(elements: list, object) -> tuple:
    return tuple(
        position for position, element in enumerate(elements) if type(element) == object
    )


def match_pairs(target: list, pattern: list) -> bool:
    return all(map(lambda t, p: t == p or isinstance(p, AnyElement), target, pattern))


def check_matching_elements(target, pattern):
    if len(target) == len(pattern) and not has_type(pattern, ManyElement):
        return match_pairs(target, pattern)

    find_positions = find_element_type_position(pattern, ManyElement)
    if len(find_positions) == 1:
        return match_pairs(target, pattern[: find_positions[0]]) and match_pairs(
            target[::-1], pattern[: find_positions[0] : -1]
        )
    else:
        raise ValueError("Too Many type ManyElement")


matching_group = [1, 2, 3, 4, 5]
matched_group1 = [1, 2, 3, any_element, 5]  # 返回 True
matched_group2 = [1, many_element, 5]  # 返回 True
matched_group3 = [5, many_element]  # 返回 False
matched_group4 = [many_element, 4]  # 返回 False
matched_group5 = [1, many_element, 4, 5]  # 返回 True

if check_matching_elements(matching_group, matched_group1):
    print("matched_group1 匹配")
else:
    print("matched_group1 不匹配")

if check_matching_elements(matching_group, matched_group2):
    print("matched_group2 匹配")
else:
    print("matched_group2 不匹配")

if check_matching_elements(matching_group, matched_group3):
    print("matched_group3 匹配")
else:
    print("matched_group3 不匹配")

if check_matching_elements(matching_group, matched_group4):
    print("matched_group4 匹配")
else:
    print("matched_group4 不匹配")

if check_matching_elements(matching_group, matched_group5):
    print("matched_group5 匹配")
else:
    print("matched_group5 不匹配")
