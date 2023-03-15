#!/usr/bin/ python3
import sys
import string


def text_analyzer(*args):
    """Counts the number of upper, lower, punctuation and space characters."""
    if len(args) > 1:
        print("ERROR")
        return
    if (len(args) == 0):
        print("What is the text to analyse?")
        print(">> ", end="")
        sys.stdout.flush()
        str = sys.stdin.readline()
    else:
        str = args[0]
    for i in range(len(str)):
        i = 0
        upper = 0
        lower = 0
        punct = 0
        space = 0
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1
        elif str[i] in (' ', '\t', '\r', '\v', '\f'):
            space += 1
        elif str[i] in (string.punctuation):
            punct += 1
    print("The text contains {} characters:".format(len(str)))
    print("- {} upper letters".format(upper))
    print("- {} lower letters".format(lower))
    print("- {} punctuation marks".format(punct))
    print("- {} spaces".format(space))



