import sys
from itertools import permutations, combinations
sys.stdin = open('../../input.txt', 'r')

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def get_team_s(m, m2, gap):
    team_s = 0
    team_l = 0
    print('================= start . ', m, m2)
    for i,j in combinations(range(len(m)), 2):
        team_s = team_s + S[m[i]][m[j]] + S[m[j]][m[i]]
    for i,j in combinations(range(len(m2)), 2):
        team_l = team_l + S[m2[i]][m2[j]] + S[m2[j]][m2[i]]
    if abs(team_s - team_l) > gap: return gap
    return abs(team_s - team_l)
gap = 999999
for members in combinations(range(N), int(N/2)): # permutations은 순열이라 combinations보다 오래걸린다
    print(members)
    start = members
    link = list(set(list(range(N))) - set(start))
    print(start, link)
    gap = get_team_s(start, link, gap)
    print('tmp : ',gap)
    if gap == 0:
        print(0)
        exit(0)

print(gap)