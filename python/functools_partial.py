from functools import partial

def f(a, b, c, x):
    return a + b + c + x


g = partial(f, 1, 2, 3)
print(g(10))

k = partial(f, 1, 2)
print(k(3, 4))

l = partial(f, 1)
print(l(2, 3, 4))
