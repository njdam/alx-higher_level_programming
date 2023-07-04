#!/usr/bin/python3
"""A file with a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """A function that prints a text with 2 new lines
    after each of these characters: '.', '?' and ':'
    and no spaces at end or start of each printed line

    Parameter:
        text (str): is text indenation and must be a string

    Raise:
        TypeError: if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punct = ['.', '?', ':']
    lens = len(text)
    i = 0
    while i in range(lens) and text[i] == ' ':
        i += 1

    while i in range(lens):
        print(text[i], end="")

        if text[i] in punct or text[i] == '\n':
            if text[i] in punct:
                print('\n')
            i += 1
            while i in range(lens) and text[i] == ' ':
                i += 1
            continue
        i += 1
