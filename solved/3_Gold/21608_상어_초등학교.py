import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")

N = int(sys.stdin.readline())
NN = pow(N, 2)
student={}
seat = [[0]*N for _ in range(N)]
dx, dy = (0,0,1,-1),(1,-1,0,0)
def seats(id):
    fav = {}
    queue = deque()
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0:
                queue.append((i,j))
                while queue:
                    x, y = queue.popleft()
                    if (x, y) not in fav.keys():
                        fav[(x, y)] = 0
                        for d in range(4):
                            nx, ny = x+dx[d], y+dy[d]
                            if nx <0 or ny<0 or nx >=N or ny>=N: continue
                            if seat[nx][ny] == 0:
                                fav[(x,y)] += 1
                                queue.append((nx,ny)) # 비어있는 공간만 탐색
                            elif seat[nx][ny] in student[id]:
                                fav[(x,y)] += 4
    print(fav)
    print(max(fav, key=fav.get))
    print('최댓값 위치들: ',[k for k,v in fav.items() if max(fav.values()) == v])
    print('최소 행렬: ',min([k for k,v in fav.items() if max(fav.values()) == v]))
    j, k = max(fav, key=fav.get)
    seat[j][k] = id

    for _ in seat:
        print(_)
def chk_satisfaction():
    happy = 0
    for i in range(N):
        for j in range(N):
            id = seat[i][j]
            cnt = 0
            for d in range(4):
                nx, ny = i+dx[d], j+dy[d]
                if nx <0 or ny<0 or nx >=N or ny>=N: continue
                if seat[nx][ny] in student[id]:
                    cnt+=1
            if cnt>0:
                happy += pow(10, cnt-1)
    print('result : ', happy)

for i in range(NN): #학생들
    id, f1, f2, f3, f4 = map(int, sys.stdin.readline().split())
    student[id] = [f1, f2, f3, f4]
    print(id)
    if i == 0: seat[1][1] = id #첫번째 학생
    else: seats(id)
chk_satisfaction()

