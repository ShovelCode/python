import inspect

#with python 3.5 you can be explicit in parameter signatures
def example_function(param1: int, param2: str) -> bool:
    pass

signature = inspect.signature(example_function)
print(signature)
