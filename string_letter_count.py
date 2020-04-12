'''
Take a string str and return a string that is made up of the number of occurances of each english letter in str,
followed by that letter. The string shouldn't contain zeros; leave them out.

An empty string, or one with no letters, should return an empty string.

Notes
Ignore all case
str will never be null
Examples
"This is a test sentence."  =>  "1a1c4e1h2i2n4s4t"
""  =>  ""
"555"  =>  ""
'''

##########################################################################################################################################
s = "AAAAssssaaasdfsd[][]((0-asdfasdojxocjvopallml sdkf[pasdk sdfk[pasdokf "


def string_letter_count(s):
    s = [i.lower() for i in s if i.isalpha()]
    s.sort()
    if not s:
        return ''
    s1 = ""
    x = s[0]
    cnt = 0
    for i in s:
        if i == x:
            cnt += 1
        else:
            s1 += (str(cnt) + x)
            cnt = 1
            x = i

    return s1 + str(cnt) + x


print(string_letter_count(s))