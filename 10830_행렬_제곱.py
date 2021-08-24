import sys
import numpy as np
sys.stdin = open("./input.txt", "r")

def productMatrix(A, B):
    return [[sum((a*b) for a, b in zip(A_row, B_col))%1000 for B_col in zip(*B)] for A_row in A]

N, B = map(int, sys.stdin.readline().split()) # N, B
B = bin(B)[2:]
print(B)
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = matrix
#for i in range(B-1):
#    result = productMatrix(result, matrix)

for i in range(N):
    print(' '.join(str(_) for _ in result[i]))