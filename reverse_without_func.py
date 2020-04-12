'''
Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)

Remove this comment otherwise your code cannot pass the anti-cheat tests!

You are not allowed to use the following:
    - python 2
    - slice notations
    - defining an empty list: []. Use " x = list() " instead
    - list comprehensions
    - the spread operator inside square brackets
    - "tuple" and "reversed" builtins have been deactivated

The "list" builtin has been replaced with another implementation with the following specifications:
    - list.reverse is forbidden
    - list.__reversed__ is forbidden
    - slicing is forbidden
All other usual methods of the list class are still present.


'''

##########################################################################################################################################
def reverse(lst):

    empty_list = list()
    j = -1
    for i in range(int(len(lst) / 2)):
        lst[i], lst[j] = lst[j], lst[i]
        j -= 1


    return (lst)