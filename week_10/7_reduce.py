from functools import reduce


def add_nums(x, y): return x + y


def example_1():
    print(reduce(add_nums, range(11)))
    print(type(reduce(add_nums, range(11))))


def example_2():
    print(reduce(add_nums, range(11)))
    print(type(reduce(add_nums, range(11))))
    print(reduce(add_nums, range(11), 10))


example_1()
example_2()