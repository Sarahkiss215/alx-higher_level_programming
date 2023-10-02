#!/usr/bin/python3
""" Prints a text with 2 new lines """


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:.,?,:"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    len_text = len(text)
    char = ".?:"
    index = 0
    line_no = ""

    while True:
        while index < len_text and text[index] == " ":
            index += 1
        if index == len_text:
            break

        start = index
        while index < len_text and text[index] not in char:
            index += 1

        if index == len_text:
            index -= 1
            while index > start and text[index] == " ":
                index -= 1

        index += 1

        first_line = text[start:index]
        if first_line:
            line_no += first_line
            if first_line[index - start - 1] in char:
                line_no += "\n\n"

    print(line_no, end="")
