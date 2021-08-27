import sys

sys.stdin = open("../../input.txt", "r")

N, K = map(int, sys.stdin.readline().split()) # N, K
if N==K or K==0: print('1')
else:
    dp = {_:[1 for _ in range(K+1)] for _ in range(N+1)}
    for i in range(1, K+1):
        for j in range(i+1, N+1):
            dp[j][i] = (dp[j-1][i-1] + dp[j-1][i]) % 10007
    print(dp[N][K])
