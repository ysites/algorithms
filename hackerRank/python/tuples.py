'''
tuples.py

Tuples Challenge on HackeRrank python
https://www.hackerrank.com/challenges/python-tuples

Given an integer, n , and n space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: uses Python 2
'''
if __name__ == '__main__':
    n = int(raw_input()) # get input from user
    t = tuple(map(int, raw_input().split()))

print hash(t)
