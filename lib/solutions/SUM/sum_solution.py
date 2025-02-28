# noinspection PyShadowingBuiltins,PyUnusedLocal
def sum_solution(x: int, y: int) -> int:
    if type(x) is not int or type(y) is not int:
        raise ValueError("Input not an integer")
    if x not in range(0, 100) or y not in range(0, 100):
        raise ValueError("Input out of range")
    return x + y


