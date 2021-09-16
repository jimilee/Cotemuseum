import sys

#다이나믹 프로그래밍, # 브루투 포스
sys.stdin = open('../../input.txt', 'r')

N = int(sys.stdin.readline())
schedule = {}
dp = []
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    schedule[i] = [t, p]
    dp.append(p)
dp.append(0)
for i in range(N - 1, -1, -1):
    if schedule[i][0] + i > N: #시간이 초과일때
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], schedule[i][1] + dp[i + schedule[i][0]])
print(dp[0])