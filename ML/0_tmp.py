import inspect

def example_func(a, b, c=10, *args, **kwargs):
    pass

params = inspect.signature(example_func).parameters
print(params)


def example_func(a, b, c=10, *args, **kwargs):
    print(locals())  # Wyświetla słownik z wszystkimi argumentami i ich wartościami

example_func(1, 2, 3, 4, 5, key="value")