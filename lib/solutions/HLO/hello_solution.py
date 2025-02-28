

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(input_string: str) -> str:
    if not isinstance(input_string, str):
        raise TypeError(f"Input {input_string} must be a string")
    return "Hello, World!"


