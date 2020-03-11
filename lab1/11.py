#!/usr/bin/python
import collections

wordcount = collections.Counter()
with open("test.txt") as file:
    for line in file:
        wordcount.update(line.split())

for k,v in wordcount.elements():
    print(k, v)