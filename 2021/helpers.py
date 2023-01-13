from functools import wraps
from time import time


def timeit(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        tf = time()
        print(f'func:{f.__name__} took: {tf-ts} seconds')
        return result
    return wrap
