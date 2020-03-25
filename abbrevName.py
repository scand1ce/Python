'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F

'''

##########################################################################################################################################

def abbrevName(name):
    name = name.upper()
    name1 = name.split()

    return (name1[0][0] + "." + name1[1][0])

print (abbrevName(name))

