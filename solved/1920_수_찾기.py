import sys

sys.stdin = open("../input.txt", "r")

N = sys.stdin.readline()#갯수 N
A = {_:1 for _ in list(map(int, sys.stdin.readline().split()))}
M = sys.stdin.readline() #갯수 M
findList = list(map(int, sys.stdin.readline().split()))
for num in findList:
    try:
        if A[num]: print('1')
    except:
        print('0')