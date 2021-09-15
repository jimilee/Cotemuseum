import sys

sys.stdin = open('../../input.txt', 'r')
N = int(sys.stdin.readline())
dx, dy = (0,1,0,-1),(-1,0,1,0)
sandout = 0
ratios = [{(-1,0):0.07, (1,0):0.07, (-1,-1):0.1, (1,-1):0.1, (0,-2):0.05, (-2,0): 0.02, (2,0): 0.02, (-1,1):0.01, (1,1):0.01},
          {(0,-1):0.07, (0,1):0.07, (1,-1):0.1, (1,1):0.1, (2,0):0.05, (0,-2): 0.02, (0,2): 0.02, (-1,-1):0.01, (-1,1):0.01},
          {(-1,0):0.07, (1,0):0.07, (-1,1):0.1, (1,1):0.1, (0,2):0.05, (-2,0): 0.02, (2,0): 0.02, (-1,-1):0.01, (1,-1):0.01},
          {(0,-1):0.07, (0,1):0.07, (-1,-1):0.1, (-1,1):0.1, (-2,0):0.05, (0,-2): 0.02, (0,2): 0.02, (1,-1):0.01, (1,1):0.01}]
def sand(x, y, alpha, board, d):
    global sandout
    yx, yy = y
    xx, xy = x
    ax, ay = alpha

    print('x, ({0},{1})  y, ({2},{3})  alpha, ({4},{5})  direc, {6}'.format(xx,xy,yx,yy,ax,ay,d))
    sand = board[yx][yy]
    board[yx][yy] = 0
    remain = sand

    for loc, ratio in ratios[d].items():
        rx, ry = yx + loc[0], yy + loc[1]
        this_sand = int(sand * ratio)
        remain -= int(sand * ratio)
        if rx < 0 or ry < 0 or rx >=N or ry >= N: #나갔을 경우
            sandout += this_sand
        else:
            board[rx][ry] = board[rx][ry] + this_sand
    if ax < 0 or ay < 0 or ax >=N or ay >= N: #나갔을 경우
        sandout += remain
    else:
        board[ax][ay] = board[ax][ay] + remain
    return board


def tornado(board):
    count = 1
    nloc = (int((N-1)/2),int((N-1)/2))
    while True:
        for d in range(4):
            if d < 2 : hol = 1
            else: hol = 0
            for i in range(hol,count+1): #이동 수
                x, y = nloc
                nx, ny = x+dx[d], y+dy[d]
                if nx < 0 or ny < 0 or nx>=N or ny>=N: continue
                if x == 0 and y == 0: return
                print('before process ... x, ({0},{1})  y, ({2},{3})  alpha, ({4},{5})  direc, {6}'.format(x,y,nx,ny,nx+dx[d],ny+dy[d],d))
                new_board = sand((x,y), (nx,ny), (nx+dx[d],ny+dy[d]), board, d)
                # new_board[nx][ny] = board[x][y]
                print(i,',', count,': ', x,',',y, ' => ', nx,',', ny)
                nloc = (nx,ny)
                board = new_board
        count += 2

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tornado(board)
print(sandout)