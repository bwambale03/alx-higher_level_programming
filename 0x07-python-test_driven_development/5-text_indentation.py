#!/usr/nin/python3
"""defines a text function indentation"""


def text_indentation(text):
    """print text with two new lines after each '.', '?' and ':'.

    Args:
    text(string): The text to print.
    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text and text[c] == ' ':
            c += 1

    while c < len(text):
    print(text[c], end="")
    if(text[c] == "\n" or text[c] in ".?:":
        if text[c] in ".?:":
        print("")
        c += 1
        while c < len(text) and text[c] == ' ':
        c += 1
        continue
        c += 1
