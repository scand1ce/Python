'''
The objective is to return all pairs of integers from a given collection of integers that have a difference of 2.

The result should be sorted in ascending order.

The input will consist of unique values. The order of the integers in the input collection should not matter.

Examples
[1, 2, 3, 4]      -->  [[1, 3], [2, 4]]
[4, 1, 2, 3]      -->  [[1, 3], [2, 4]]
[1, 23, 3, 4, 7]  -->  [[1, 3]]
[4, 3, 1, 5, 6]   -->  [[1, 3], [3, 5], [4, 6]]

'''

##########################################################################################################################################
lst = [1, 3, 4, 6]


# [1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56]
# [1, 3, 4, 6]

def twos_difference(lst):
    arr = []
    lst.sort()
    c = 1
    while c < len(lst[:-1]):
        for i in range(0, len(lst)):

            if c + 1 <= len(lst) and lst[i + 1] - lst[i] == 2:
                arr.append(tuple([lst[i], lst[i + 1]]))

            if c + 2 <= len(lst) and lst[i + 2] - lst[i] == 2:
                arr.append(tuple([lst[i], lst[i + 2]]))

            c += 1

    return arr


print(twos_difference(lst))