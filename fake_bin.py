'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

'''

##########################################################################################################################################

def fake_bin(x):
    arr_i = []
    arr_c = []
    while len(arr_i) < len(x):
        for i in x:
            arr_i.append(int(i))
    while len(arr_c) < len(x):
        for c in arr_i:
            if c < 5:
                arr_c.append(str(0))
            if c >= 5:
                arr_c.append(str(1))
        x_new = ''.join(arr_c)
        return x_new






