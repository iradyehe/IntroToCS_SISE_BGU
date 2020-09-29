def len_3():
    my_li2 = [[1, 2, 3], [4, 5], [6, 7, 8]]
    for i in range(3):
        for j in range(len(my_li2)):
            if i < len(my_li2[j]):
                print(my_li2[j][i])


def add_number():
    my_li2 = [[1,2,3],[4,5],[6,7,8,10000]]

    for i in range(3):
        for j in range(len(my_li2)):
            if i<len(my_li2[j]):
                print(my_li2[j][i])


def longest_column():
    my_li2 = [[1,2,3],[4,5],[6,7,8,10000]]

    longest_col = 0
    for i in range(len(my_li2)):
        if len(my_li2[i])>longest_col:
            longest_col = len(my_li2[i])

    for i in range(longest_col):
        for j in range(len(my_li2)):
            if i<len(my_li2[j]):
                print(my_li2[j][i])


# len_3()
# add_number()
# # longest_column()