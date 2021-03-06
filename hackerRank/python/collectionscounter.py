'''
collectionscounter.py

collections.Counter() HackerRank Problem Solution

https://www.hackerrank.com/challenges/collections-counter/problem

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Concepts reviewed:

1. collections.Counter() - A counter is a container that stores elements as dictionary keys,
and their counts are stored as dictionary values.

'''
import collections

# number of shoes
X = int(raw_input())

sizes = collections.Counter(map(int, raw_input().split()))

#number of customers
N = int(raw_input())

#amount of money earned by Raghu
money = 0

#fill the list with user's input
for i in range(N):
    (size, price) = map(int, raw_input().split())

#calculate the total amount of money made by Raghu
    if sizes[size] > 0:
        sizes[size] -= 1
        money += price

print money
