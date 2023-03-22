from collections import deque
import sys

sys.stdin = open('./input.txt', 'r')
# dfs + 배낭문제 섞어서 풀어보기.
dx, dy = (-1,-1,0,1,1,1,0,-1),(0,-1,-1,-1,0,1,1,1)
board = {}
for i in range(4):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        board[(i,j)] = data[j*2:2]
print(board)


def shark_move(shark_info):
    loc, d = shark_info
    x, y = loc
    fish = []
    while True:
        nx, ny = x+dx[d], y+dy[d]
        if board[(nx,ny)][0] != -1: # 물고기가 있을때.
            fish.append(board[(nx,ny)])