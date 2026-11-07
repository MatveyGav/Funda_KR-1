def counter(func):
    def decorator(*args, **kwargs):
        decorator.count += 1
        return func(*args, **kwargs)
    decorator.count = 0
    return decorator

@counter
def f():
    pass

@counter
def hello_world():
    print('hello world')
