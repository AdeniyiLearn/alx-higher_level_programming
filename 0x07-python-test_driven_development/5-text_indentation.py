#!/usr/bin/python3

""" Module contains the function text_indentation

test_indentation : is a function that prints a text with 2 new lines after characters: . ? and :

prototype
---------

test_indentation()

Usage:
------

>>> test_indentation("hello peopel: how are you?")
"""

def text_indentation(text):
    """Function that print 2 new lines for characters: . ? :
        
        parameter:
                text: a string of text
        Returns:
                None
    """
    if not isinstance(text, str):
        raise TypeError ("text must be a string")
    for i in range(len(text)):
        if not text[0] == ' ':
            i += 1
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i] + "\n")
            if text[i + 1] == ' ':
                i += 2

        else:
            print(text[i], end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("test/4-print_square.txt")

