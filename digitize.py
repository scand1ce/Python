'''
Convert number to reversed array of digits
Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]

'''

##########################################################################################################################################

def digitize(n):
    n = str(n)
    n = n[::-1]
    n = n.replace('',' ')
    l = len(n)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = n[i]

        while '0' <= a <= '9':
            s_int += a
            i += 1

            if i < l:
                a = n[i]

            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))


    return integ



