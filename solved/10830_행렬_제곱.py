import sys
sys.stdin = open("../input.txt", "r")

def productMatrix(A, B):
    return [[sum((a*b) for a, b in zip(A_row, B_col))%1000 for B_col in zip(*B)] for A_row in A]

def recursive_pow(C,n):
    if n == 1:
        identity_matrix = [[1 if i==j else 0 for j in range(N)] for i in range(N)]
        return productMatrix(C,identity_matrix)
    if n % 2 == 0:
        y = recursive_pow(C, n/2)
        return productMatrix(y,y)
    else:
        y = recursive_pow(C, (n-1)/2)
        return productMatrix(productMatrix(y,y), C)

N, B = map(int, sys.stdin.readline().split()) # N, B
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = recursive_pow(matrix, B)
for i in range(N):
    print(' '.join(str(_) for _ in result[i]))