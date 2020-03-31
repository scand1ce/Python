'''
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity
'''

##########################################################################################################################################
s = "abcdadfgdfgadfgef"

def capitalize(s):
    arr = []
    arr2 = []
    c = 0
    c1 = 0
    while c < len(s):
        for j in s:
            if c%2 == 0 or c == 0:
                arr.append(j.upper())
            elif c%2 != 0:
                arr.append(j.lower())


            c+=1

    while c1 < len(s):
        for x in s:
            if c1 % 2 == 0 or c1 == 0:
                arr2.append(x.lower())
            elif c1%2 != 0:
                arr2.append(x.upper())



            c1+=1

    return [''.join(arr),''.join(arr2)]

print(capitalize(s))
###############################################################################
def capitalize(s):
    result = ['','']
    for i,c in enumerate(s):
        result[0] += c.lower() if i % 2 else c.upper()
        result[1] += c.upper() if i % 2 else c.lower()
    return result