from typing import Callable


def extract_variable(*variable: int) -> Callable[[Callable], Callable]:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            user = func(*args, **kwargs)
            print(user, *variable)
            return func(*args, **kwargs)

        return wrapper

    return decorator


my_variable = extract_variable(1, 2, 3, 4, 5, 6)


@my_variable
def function(name: str) -> str:
    return f"my name is {name}"


print(function("ABC"))
