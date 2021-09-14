import sys
from collections import deque
from itertools import combinations

sys.stdin = open('../../input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())

#필수로 알아야하는 단어들
known = {'a','n','t','i','c'}
if K < 5:
    print(0)
    exit(0)
elif K == 26:
    print(N)
    exit(0)
else: K -= 5
#org = [set(sys.stdin.readline().rstrip()) for _ in range(N)]
org = {ky: v for v, ky in enumerate(
    (set(map(chr, range(ord('a'), ord('z')+1))) - known))} #ord - 아스키코드
print(org)
cnt = 0
know = []
for _ in range(N):
    tmp = 0
    for c in set(input())-known:
        print(c)
        tmp |= (1 << org[c])
    know.append(tmp)
power_by_2 = (2**i for i in range(21))
for comb in combinations(power_by_2, K):
    test = sum(comb)
    print(test)
    ct = 0
    for cb in know:
        if test & cb == cb:
            ct += 1
    cnt = max(cnt,ct)
print(cnt)

#
# for w in org:
#     for a in w:
#         if a not in words.values() and a:
#             words[cnt] = a
#             cnt+=1
# len_words = cnt
# print('len_words', cnt)
# print(words)
# def cnt_known_word(know):
#     print(' start cnt_known')
#     print(know)
#     cnt = 0
#     for word in org:
#         flag = True
#         for k in word:
#             if k not in know:
#                 flag = False
#                 break
#         if flag: cnt += 1
#     return cnt
#
# visited = [False] * len_words
# max = 0
# know = ['']*K
# def comb(cnt):
#     global max
#     if cnt == K:
#         print('know_ list :', know, cnt)
#         know_cnt = cnt_known_word(know)
#         print(know_cnt, ' . . . after cnt_known_word')
#         if know_cnt > max:
#             max = know_cnt
#         return
#
#     for i in range(len_words):
#         if visited[i]: continue
#         visited[i] = True
#         know[cnt] = words[i]
#         comb(cnt+1)
#         visited[i] = False
#
# comb(0)
# print(max)
