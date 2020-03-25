'''
You will be given an vector of string(s). You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

'''

##########################################################################################################################################

def two_sort(array):
    array.sort()
    array = array[0]
    array = array.replace('', '***')
    array = array[3:-3]
    return array

##############################################################################################################################################
def two_sort(lst):
    return '***'.join(min(lst)) def two_sort(lst):




