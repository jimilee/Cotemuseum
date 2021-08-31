import sys
sys.stdin = open("./input.txt", "r")

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for _ in board:
    print(_)

blocks = {'blue':[[(0,0),(0,1),(0,2),(0,3)],   [(0,0),(1,0),(2,0),(3,0)]],

          'yellow':[[(0,0),(0,1),(1,0),(1,1)]],

          'orange':[[(0,0),(1,0),(2,0),(2,1)],  [(0,0),(0,1),(0,2),(1,0)],
                    [(0,0),(0,1),(1,0),(2,0)],  [(0,0),(1,0),(1,1),(1,2)],
                    [(0,0),(0,1),(1,1),(2,1)],  [(1,0),(1,1),(0,2),(1,2)],
                    [(0,1),(1,1),(2,1),(2,0)],  [(0,0),(0,1),(0,2),(1,2)]],

          'green':[[(0,0),(1,0),(1,1),(2,1)],   [(1,0),(1,1),(0,1),(0,2)],
                   [(0,1),(1,1),(1,0),(2,0)],   [(0,0),(0,1),(1,1),(1,2)]],

          'pink':[[(0,0),(0,1),(0,2),(1,1)],   [(0,0),(1,0),(1,1),(2,0)],
                  [(1,0),(1,1),(0,1),(2,1)],   [(0,1),(1,0),(1,1),(1,2)]]}

def check_blocks(x, y):
    max_val = 0
    box = 0
    for key, item in blocks.items():
        for roc in item:
            print('try another block.')
            box = 0
            for i in range(4):
                nx, ny = x+roc[i][0], y+roc[i][1]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    print(nx, ny, ' is out of board.')
                    break
                box += board[nx][ny]
                print(board[nx][ny])
            if max_val < box: max_val = box
            print('box : ', box)
            print('max_val : ', max_val)
    return max_val

result = 0
for x in range(N):
    for y in range(M):
        max_val = check_blocks(x, y)
        if result < max_val: result = max_val
print('result : ', result)