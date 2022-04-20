import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

def combination(array, r):
    for i in range(len(array)):
        if r == 1: #종료
            yield [array[i]]
        else:
            for next in combination(array[i+1:], r-1):
                yield [array[i]]+next

