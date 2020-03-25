'''
Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. 
First argument is an array of numbers and the second is the divisor.

Example
divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]

'''

##########################################################################################################################################

numbers = [0, 1, 2, 3, 4, 5, 6, 7]
divisor = 2

def divisible_by(numbers, divisor):


    filter_obj = filter(lambda numbers: numbers % divisor == 0, numbers)

    even_num = list(filter_obj) 

    return even_num

print (divisible_by(numbers, divisor))
