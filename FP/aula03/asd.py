
# Given a string, find all integers inside and return a string that separates them by commas.
# Words and numbers will be separated by a single space. There should be no leading or
# trailing commas. For example, if 11 12 and 13 are in the string, you should return
# '11,12,13' NOT '11,12,13,' or ',11,12,13'. If no integers are found, return an empty string.


def numbersInside(s):
    str = ''
    for i in s.split():
        if i.isdigit():
            str += i + ','
    return str[:-1]