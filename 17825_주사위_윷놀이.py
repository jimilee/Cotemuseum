import copy
import sys
from collections import deque

sys.stdin = open("./input.txt", "r")
board = {}
for i in range(0,44,2):
    board[i] = [i+2]
    if i == 10 or i == 16: #블루 라인
        board[i].extend([i+3])
    if i == 20 : #블루 라인
        board[i].extend([i+2])
    if i == 22:
        board[i].extend([24])
    if i == 24:
        board[i].extend([25])
    if i == 26:
        board[i].extend([25])
    if i == 28:
        board[i].extend([27])
    if i == 30:
        board[i].extend([i-2])
board[13] = [-1,16]
board[19] = [-1,25]
board[27] = [-1,26]
for i in range(25, 41, 5):
    try: board[i].extend([i+5])
    except: board[i] = [-1,-1,i+5]


blue_line = [10,20,30]
black_line = [25]
def permutation(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutation(array[i:]+array[:i], r-1):
                yield [array[i]]+next

dice = list(map(int, sys.stdin.readline().split()))
max_score = 0
result = []
# for trial, sel in enumerate(permutation(list(range(4)),10)):
for trial, sel in enumerate(permutation(list(range(4)),10)):
    # if trial > 1: break
    # print(sel)
    horse = [0,0,0,0] # 초기 말 위치
    state_horse = [0,0,0,0] # 라인 상태
    score = 0
    flag = True
    for turn, idx in enumerate(sel):
        # print('============== turn ', turn)
        # print('  선택 된 말 id . : ', idx)
        # print(horse)
        others = []
        for _ in range(4):
            if idx != _:
                others.append(horse[_])
            else: others.append(-1)
        # print(others)
        horse_loc = horse[idx]
        horse_st = state_horse[idx]
        if horse_st == -1: # 이미 종점까지 도달함.
            # print('해당 말 선택 불가.')
            flag = False
            break
        # print('주사위 수 : ',dice[turn])
        # print('   말 이동 ... ')
        # print('현재 위치 : ',horse_loc, '경로 ', horse_st)

        for _ in range(dice[turn]): # 말 이동
            # print(horse_loc, horse_st)
            if horse_loc >= 40:
                # print('말 도착!')
                state_horse[idx] = -1
                horse[idx] = 41
                break
            if horse_loc in black_line:
                horse_st = 2
            horse_loc = board[horse_loc][horse_st]
        # # print(horse)
        # print('---말 이동 완료')
        # print('현재 위치 : ',horse_loc, '경로 ', horse_st)

        if state_horse[idx]!=-1:
            horse[idx] = horse_loc
            state_horse[idx] = horse_st
            score += horse_loc
            # print('score : ', score)
            if horse[idx] in blue_line and horse_st == 0:
                # print('현재말 위치. ', horse[idx], '상태 ->', 1)
                state_horse[idx] = 1
            elif horse[idx] in black_line:
                # print('현재말 위치. ', horse[idx], '상태 ->', 2)
                state_horse[idx] = 2
        if horse_loc in others:
            # print('해당 말 선택 불가.', others.index(horse_loc))
            # print(others)
            # print(state_horse)
            # print(horse_loc)
            # print(horse_st)
            # print(state_horse[idx])
            # print(state_horse[others.index(horse_loc)] == state_horse[idx])
            if state_horse[others.index(horse_loc)] == state_horse[idx] or horse_loc == 40:
                flag = False
                break

            # else:
            #     state_horse[idx] = 0
        # print(state_horse)
    if flag:
        # print(" 해당 턴 완료 . ")
        if score>max_score:
            max_score = score
            result = sel
            print('현재 score : ', score, max_score)
            print(sel)

print(max_score)