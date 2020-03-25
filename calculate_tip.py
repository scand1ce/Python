'''
Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%
The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#
Because you're a nice person, you always round up the tip, regardless of the service.

'''

##########################################################################################################################################

def calculate_tip(amount, rating):
    z = rating.capitalize()
    import math
    if z == 'Terrible':
        return 0
    elif z == 'Poor':
        z = amount*0.05

        return math.ceil(z)

    elif z == 'Good':
        z = amount*0.1
        return math.ceil(z)

    elif z == 'Great':
        e = amount*0.15
        return math.ceil(e)

    elif z == 'Excellent':
        e = amount * 0.2
        return math.ceil(e)

    else:
        return 'Rating not recognised'

    return z

