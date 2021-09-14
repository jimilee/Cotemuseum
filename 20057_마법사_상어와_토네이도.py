import sys

sys.stdin = open('./input.txt', 'r')
N = int(sys.stdin.readline())
dx, dy = (0,1,0,-1),(-1,0,1,0)
def tornado(board, loc):
    new_board = [[0]*N for _ in range(N)]
    x, y = loc
    count = 0
    while True:
        if x == 0 and y == 0: break
        for d in range(4):
            if d < 2 : hol = 1
            else: hol = 0
            print('hol', hol, ' direcntion', dx[d],dy[d])
            for i in range(hol,count,2): #회전수
                print(i)
                nx, ny = x+dx[d], y+dy[d]
                # if nx < 0 or ny < 0 or nx>=N or ny>=N: continue
                # new_board[nx][ny] = board[x][y]
                x, y = nx, ny
        count += 1

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
center_pt = int(N/2)

tornado(board, (center_pt, center_pt))