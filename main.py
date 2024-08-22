def filter_strings(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            result = [item for item in result if not isinstance(item, str)]
        return result

    return wrapper


@filter_strings
def example_function():
    return [1, "Hlsad  al", 3.14, "qweqwads ", 42, "asdadasd", "EQewE"]


@filter_strings
def example_non_list():
    return "Its not a list"


print(example_function())
print(example_non_list())
