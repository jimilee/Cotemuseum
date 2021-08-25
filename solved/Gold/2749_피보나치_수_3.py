import sys

#피사노 주기
#1000000 (백만) 으로 나눈 나머지 피보나치 수열의 반복주기는 1500000 (150만)
sys.stdin = open("../../input.txt", "r")

N = int(sys.stdin.readline()) # N

FIBONACCI = [0]*1500050
FIBONACCI[0] = 0
FIBONACCI[1] = 1
def fibonacci(N):
    for i in range(1500000):
        FIBONACCI[i+2] = (FIBONACCI[i+1] + FIBONACCI[i])%1000000
    print(FIBONACCI[N%1500000])

fibonacci(N)