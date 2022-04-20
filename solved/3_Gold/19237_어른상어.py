import copy
import sys

sys.stdin = open('../../input.txt', 'r')

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M, k = map(int, input().split())
print(N, M, k)
board = [list((map(int, sys.stdin.readline().split()))) for _ in range(N)]
shark_board = [[0]*N for _ in range(N)]


# 상어 위치 & 이동 카운트
sharks_loc = {}
for low, val in enumerate(board):
    for col, i in enumerate(val):
        if i != 0:
            sharks_loc[i] = (low, col)
            shark_board[low][col] = k+1
print('sharks_loc\n',sharks_loc)

# 상어 방향
sharks_dir = { s_id+1 :dir for s_id, dir in zip(range(M), list(map(int, input().split())))}
print('sharks_dir\n',sharks_dir)
# 상어 우선순위
sharks = {}
id = 1
for p in range(M * 4):
    try:
        sharks[id].append(list(map(int, sys.stdin.readline().split())))
    except:
        sharks[id] = []
        sharks[id].append(list(map(int, sys.stdin.readline().split())))
    if len(sharks[id]) == 4:
        id+=1

print('sharks\n',sharks)

def level_check(nx, ny, out_shark, id):
    winner = id
    print('level_check')
    print("board : ")
    for _ in board:
        print(_)
    print("shark_board : ")
    for _ in shark_board:
        print(_)
    if board[nx][ny] < id and shark_board[nx][ny] == k + 1:  # 자신의 상어 id보다 작은상어의 냄새가 나면 쫒겨남
        print('\n높은 레벨 상어 발견.')
        out_shark.append(id)
        winner = board[nx][ny]
    if board[nx][ny] > id and shark_board[nx][ny] == k + 1:  # 자신의 상어 id보다 큰 상어의 냄새가 나면 쫒음
        print('\n낮은 레벨 상어 발견.')
        out_shark.append(board[nx][ny])
    return out_shark, winner

def move_sharks(board, shark_board, sharks_dir, sharks_loc):
    out_shark = []
    for id in sharks_loc.keys():
        print("\n\n 지금 id ", id)
        x, y = sharks_loc[id]
        print('현재 상어 방향 ',sharks_dir[id])
        print('현재 상어 위치 ', x,y)
        priority = sharks[id][sharks_dir[id]-1] # 상어 움직임 우선순위
        flag = False
        for s in range(2): # 총 2단계 우선순위
            if flag:
                break
            for i in priority:
                nx, ny = x+ dx[i-1], y + dy[i-1]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                print("===========priolity : {0}===========".format(s))
                print(x, y, ' -> ', nx, ny, ' 방향 : {0}'.format(i))
                print(board[x][y] , ' -> ', board[nx][ny])
                if board[nx][ny] == 0 and s==0: # 빈칸 우선
                    # out_shark, winner = level_check(nx, ny, out_shark, id)
                    # print(out_shark, winner)
                    sharks_loc[id] = (nx, ny)
                    sharks_dir[id] = i
                    # board[nx][ny] = winner
                    flag = True
                    break
                if board[nx][ny] == id and s==1: # 자기 칸
                    # out_shark, winner = level_check(nx, ny, out_shark, id)
                    # print(out_shark, winner)
                    sharks_loc[id] = (nx, ny)
                    sharks_dir[id] = i
                    # board[nx][ny] = winner
                    flag = True
                    break

    # print("board : ")
    # for _ in board:
    #     print(_)
    # print("shark_board : ")
    # for _ in shark_board:
    #     print(_)
    # 상어 위치
    print('\n=========== 상어 위치 ===========')
    for id, loc in sharks_loc.items():
        print(loc, id)
        x, y = loc
        winner = id
        if shark_board[x][y] == k+1:
            out_shark, winner = level_check(x, y, out_shark, id)
        board[x][y] = winner
        shark_board[x][y] = k+1

    print(out_shark)
    # 쫒겨난 상어 삭제
    for id in out_shark:
        print('상어 삭제 : ',id)
        # for i in range(N):
        #     for j in range(N):
        #         if board[i][j] == id:
        #             board[i][j] = 0
        sharks.pop(id)
        sharks_dir.pop(id)
        sharks_loc.pop(id)


    for loc in sharks_loc:
        print(loc)
    print('현재 상어 현황 : \n',sharks_loc)
    return len(sharks_loc.keys())

def del_smell():
    print('\n상어 냄새 삭제 : ')
    for i in range(N):
        for j in range(N):
            if shark_board[i][j] > 0 :
                shark_board[i][j] -= 1  # 냄새 제거
            if shark_board[i][j] == 0:
                board[i][j] = 0
    print("board : ")
    for _ in board:
        print(_)
    print("shark_board : ")
    for _ in shark_board:
        print(_)

for _ in board:
    print(_)

times = 0
while True:
    if times >= 1000:
        print(-1)
        sys.exit(0)
    del_smell()
    num_sharks = move_sharks(board, shark_board, sharks_dir, sharks_loc)
    times += 1
    if num_sharks == 1: break
print(times)

