import sys
#페르마의 소정리.
sys.stdin = open("./input.txt", "r")
p = 1000000007
def power(a, b):
    if b==0: return 1
    if b % 2: return (power(a,b//2)**2*a)%p
    else: return (power(a,b//2)**2)%p

N, K = map(int, sys.stdin.readline().split()) # N, K
if N==K or K==0: print('1')
else:
    dp = {_:1 for _ in range(N+1)}
    for i in range(2, N+1):
        dp[i] = dp[i-1] * i % p
    print((dp[N] % p)*(power((dp[N-K] * dp[K]) % p, p-2) % p) %p)