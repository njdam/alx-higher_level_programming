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

    punct = [".", "?", ":"]
    line = ""

    for char in text:
        line += char
        if char in punct:
            line = line.strip()  # to remove trailing white space
            if line.startswith(" "):  # remove spaces where line starts
                line = line[1:]
            print("{}\n".format(line))
            line = ""  # After printing line start with empty new line

    if line.strip():  # if last_line is not empty after removing tr..sapces
        if line.startswith(" "):  # remove spaces where last line started
            line = line[1:]
        print("{}".format(line.strip()), end="")
