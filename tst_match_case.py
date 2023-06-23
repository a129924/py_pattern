def sequence(colletion):
    match colletion:
        case 1, x, *others, y:
            print(f"Got 1 and a nested sequence: x = {x}, others = {others}, y = {y}")
        case (1, x):
            print(f"Got 1 and {x}")
        case [x, y, z]:
            print(f"{x=}, {y=}, {z=}")
        case 2, [_]:
            print(colletion)


sequence([1, 2, 3, 4, 5])
