class NotFoundError(Exception):
    ...


def match_list(list1, list2):
    list1_idx = 0
    list2_idx = 0

    x = []
    y = []
    while list1_idx < len(list1) and list2_idx < len(list2):
        if list1[list1_idx] != list2[list2_idx] and list2[list2_idx] in ("x", "y"):
            if list2[list2_idx] == "x":
                x.append(list1[list1_idx])

            elif list2[list2_idx] == "y":
                if list2[min(list2_idx + 1, len(list2) - 1)] != list1[list1_idx]:
                    y.append(list1[list1_idx])
                    list1_idx += 1
                    continue

            list1_idx += 1
            list2_idx += 1
        else:
            raise NotFoundError("Not Match")
    return {"x": x, "y": y}


print(match_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 0]))
