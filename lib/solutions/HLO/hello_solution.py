

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError(f"Input {name} must be a string")
    return f"Hello, {name}!"



