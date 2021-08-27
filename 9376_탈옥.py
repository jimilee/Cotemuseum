import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

N = int(sys.stdin.readline()) # N
dx, dy = (1,-1,0,0),(0,0,1,-1)
# 테케 3번. 코스트로 어떻게 탐색할지.....
def make_path(sinner_loc, prison, H, W):
    visited = [[False for _ in range(W)] for _ in range(H)]
    queue = deque()
    queue.append(sinner_loc)
    cost = [[1 if prison[w][h] != '*' else 0 for h in range(W)] for w in range(H)]
    path_cost = {}
    path_door = {}
    cnt = 0
    opendoor = 0
    while queue:
        x, y = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or nx >= H or ny <0 or ny >= W:
                    continue
                print(nx, ny,'탐색 노드')
                if not visited[nx][ny]:
                    if prison[nx][ny] == '.' or prison[nx][ny] == '#' or prison[nx][ny] == '$':
                        if prison[nx][ny] == '#': #문일때.
                            cost[nx][ny] = cost[x][y] + 1
                            opendoor += 1
                            if cnt not in path_door.keys():
                                path_door[cnt] = [(nx,ny)]
                            else:
                                path_door[cnt].append((nx,ny))
                            queue.append((nx,ny))
                        else:
                            cost[nx][ny] = cost[x][y]
                            queue.appendleft((nx,ny))
                        if nx == 0 or nx == H-1 or ny == 0 or ny == W-1:
                            path_cost[cnt] = (opendoor, cost[nx][ny])
                            opendoor = 0
                            cnt+=1
                            print(path_door)
                            print(path_cost)
                            print('탈출!')


                        print('===========================, opendoor = ', opendoor)
                        for p in prison:
                            print(p)
                        for p in cost:
                            print(p)

    print(path_cost)
    print(path_door)
    tmp = 9999
    fin = 0
    door_num = 0
    for path, door in path_cost.items():
        if door < tmp:
            fin = path
            door_num = door
    print('result : ',fin, door_num)
    if door_num>0:
        for doors in path_door[fin]:
            x,y = doors
            prison[x][y] = '.'
    return prison, door_num

def prison_break(prison, H, W):
    remain = 2
    for i in range(H):
        for j in range(W):
            if prison[i][j] == '$':
                print('remain', remain)
                if remain == 2: #죄수 위치 파악
                    n_prison, opendoor = make_path((i,j), prison, H, W)
                    remain -= 1
                else:
                    m_prison, opendoor2 = make_path((i,j), n_prison, H, W)
                    remain -= 1
                    break
    return opendoor + opendoor2

result= []
for test_case in range(N):
    H, W = map(int, sys.stdin.readline().split())
    prison = [[_ for _ in ''.join(list(sys.stdin.readline().split()))] for _ in range(H)]
    print(' 문제 !!!! ')
    result.append(prison_break(prison, H, W))
print(result)