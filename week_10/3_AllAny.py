def example_1():
    no_one = [False, False, False]
    some_ones = [True, False, True]
    every_one = [True, True, True]
    empty_one = []
    print('any:')
    print(any(no_one))
    print(any(some_ones))
    print(any(every_one))
    print(any(empty_one))

    print('all:')
    print(all(no_one))
    print(all(some_ones))
    print(all(every_one))
    print(all(empty_one))


def example_2():
    a = [1, 2]
    b = [1, 2, 3, 4]
    l1 = [element in b for element in a]
    print(l1)


def example_3():
    a = [1, 2]
    b = [1, 2, 3, 4]
    l1 = all([element in b for element in a])
    print(l1)


example_1()
example_2()
example_3()
