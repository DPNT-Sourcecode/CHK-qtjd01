# noinspection PyShadowingBuiltins,PyUnusedLocal
def sum_solution(x: int, y: int) -> int:
    if x or y not in range[0, 100]:
        raise ValueError("Input out of range")
    return x + y
