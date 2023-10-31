#!/usr/bin/python3
'''
check each of the character
if it is not in the ASCII value of 65 - 90
convert character to integer
subtract 32 from the Integer
print the integer ASCII character value out
'''
def uppercase(c):
    for i in c:
        if ord(i) >= 65 and ord(i) <= 90 or i.isdigit() or i == ' ':
            word = i
        else:
            word = chr(ord(i) - 32)

        print("{}".format(word), end='') 

    print("")
