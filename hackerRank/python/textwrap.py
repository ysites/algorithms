'''
textwrap.py
Text Wrap HackerRank Problem Solution

Instructions:
You are given a string S  and width w.
Your task is to wrap the string into a paragraph of width w.

Concepts reviewed:
1. textwrap.fill vs textwrap.wrap - fill returns a string. wrap returns a list. 
'''

def wrap(string, max_width):
    new_string = textwrap.fill(string, max_width)
    return new_string
