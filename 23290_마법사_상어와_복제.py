import copy
import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

dx, dy = (-1, 0, 1, 0),( 0, -1, 0, 1)
fdx, fdy = (0, -1, -1, -1, 0, 1, 1, 1),\
           (-1, -1, 0,  1, 1, 1, 0, -1)
M, S = map(int, sys.stdin.readline().split())
fish_smell = [[0]*4 for _ in range(4)]
fish_cnt = [[0]*4 for _ in range(4)]

fishes = {}
new_fishes = {}
for i in range(M):
    x,y,d = map(int, sys.stdin.readline().split())
    try: fishes[(x-1,y-1)][d-1] += 1
    except:
        fishes[(x-1,y-1)] = [0]*8
        fishes[(x-1,y-1)][d-1] += 1

    fish_cnt[x-1][y-1] += 1

x, y = (map(int, sys.stdin.readline().split()))
shark = (x-1, y-1)

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combination(array[i+1:], r-1):
                yield [array[i]] + next

def permination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permination(array[i:]+array[:i], r-1):
                yield [array[i]] + next

def fish_move(fishes, new_fishes, fish_cnt):
    print(' 물고기 이동...' )
    # print(fishes)
    # print(new_fishes)
    print(shark)
    for _ in fish_cnt:
        print(_)
    print("--")
    for _ in fish_smell:
        print(_)
    print("--")
    for loc, f in fishes.items():
        for fd in range(8):
            if fishes[loc][fd] == 0 : continue

            o_fd = fd
            print('fish :', loc, fd, o_fd)
            visited = 8
            fx, fy = loc
            while True:
                nx, ny = fx + fdx[o_fd], fy + fdy[o_fd]
                visited-=1
                if visited < 0:
                    try: new_fishes[(fx,fy)][o_fd] += fishes[loc][fd]
                    except:
                        new_fishes[(fx,fy)] = [0]*8
                        new_fishes[(fx,fy)][fd] += fishes[loc][fd]
                    break
                if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 \
                        or fish_smell[nx][ny] > 0 or (nx, ny) == shark:
                    #반시계방향 회전
                    if o_fd == 0:
                        o_fd = 7
                    else:
                        o_fd -= 1
                    continue

                else: # 냄새 없고 상어 없을때
                    fish_cnt[fx][fy] -= fishes[loc][fd]
                    fish_cnt[nx][ny] += fishes[loc][fd]
                    print('fish move :', loc, fd, '->', nx, ny)
                    # print(fish_cnt[nx][ny], fishes[loc][fd])
                    # print(fishes)
                    try: new_fishes[(nx,ny)][o_fd] += fishes[loc][fd]
                    except:
                        new_fishes[(nx,ny)] = [0]*8
                        new_fishes[(nx,ny)][o_fd] += fishes[loc][fd]
                    break
    for _ in fish_cnt:
        print(_)
    return fishes, new_fishes, fish_cnt

def shark_path_finder(shark, fish_cnt, fishes, new_fishes, fish_smell):
    print('상어 이동... start')
    paths = {}
    max_count = 0
    for path in permination(list(range(4)), 3):
        visited = []
        sx, sy = shark
        # visited.append((sx,sy))
        flag = True
        cnt_f = 0
        for p in path:
            nx, ny = sx + dx[p], sy + dy[p]
            if nx<0 or ny<0 or nx>=4 or ny>=4:
                flag = False
                break
            else: # 상어 이동
                if (nx, ny) not in visited:
                    cnt_f += fish_cnt[nx][ny]
                visited.append((nx,ny))
                sx, sy = nx, ny
        #print(cnt_f, '이동 완료 : ', flag)
        if flag:
            if max_count < cnt_f:
                max_count = cnt_f
            try:
                paths[cnt_f].append(path)
            except:
                paths[cnt_f] = [path]
    # print("상어 경로...")
    res = sorted(paths[max_count])
    # print(res)
    # print(res[0])
    # for _ in fish_cnt:
    #     print(_)
    sx, sy = shark
    rm_fish = set()
    # if fish_cnt[sx][sy] > 0:
    #     fish_smell[sx][sy] = 2
    #     fish_cnt[sx][sy] = 0
    #     for idx,f in enumerate(new_fishes):
    #         fx,fy,_ = f
    #         if fx == sx and fy == sy:
    #             rm_fish.append((sx,sy,_))
    for d in res[0]:
        nx, ny = sx + dx[d], sy + dy[d]
        if fish_cnt[nx][ny] > 0:
            print('물고기 먹었다!')
            print(fish_cnt[nx][ny], '마리')
            fish_smell[nx][ny] = 3
            fish_cnt[nx][ny] = 0
            rm_fish.add((nx,ny))
        print('상어 이동 ', sx, sy, '->', nx, ny)
        sx, sy = nx, ny

    shark = (sx, sy) # 상어 이동 완료

    # print("\nfish_cnt! ")
    # for _ in fish_cnt:
    #     print(_)
    # 물고기 삭제
    print('--- 물고기 삭제. ---\n')
    print(new_fishes)
    print(rm_fish)
    for rm in rm_fish:
        new_fishes.pop(rm)

    print('--- 복제 물고기 합체 ---')
    # print(new_fishes)
    # print(fishes)
    for loc,f in fishes.items():
        fx, fy = loc
        fish_cnt[fx][fy] += sum(fishes[(fx,fy)])
        print(fx, fy, sum(fishes[(fx,fy)]), '->',fish_cnt[fx][fy])

    for _ in fish_cnt:
        print(_)

    for loc,f in new_fishes.items():
        fx, fy = loc
        for d in range(8):
            try: fishes[(fx,fy)][d] += new_fishes[(fx,fy)][d]
            except:
                fishes[(fx,fy)] = [0]*8
                fishes[(fx,fy)][d] += new_fishes[(fx,fy)][d]

    new_fishes.clear()
    # print(new_fishes)
    # print(fishes)
    return shark, fish_cnt, fishes, new_fishes, fish_smell

def smell_time(fish_smell):
    for i in range(4):
        for j in range(4):
            if fish_smell[i][j] > 0:
                fish_smell[i][j] -= 1
    return fish_smell

for i in range(S):
    print("============================!!! {0} 번째 마법 발동!!!============================".format(i))
    print('현재 상태...(물고기 수)')
    for _ in fish_cnt:
        print(_)
    print(shark)
    # 물고기 이동
    fishes, new_fishes, fish_cnt = fish_move(fishes, new_fishes, fish_cnt)
    # 상어 이동
    shark, fish_cnt, fishes, new_fishes, fish_smell = shark_path_finder(shark, fish_cnt, fishes, new_fishes, fish_smell)
    # 냄새 카운트 감소
    fish_smell = smell_time(fish_smell)
    print('현재 상태...(물고기 냄새)')
    for _ in fish_smell:
        print(_)


print('현재 상태...(물고기 수)')
for _ in fish_cnt:
    print(_)
print('현재 상태...(물고기 냄새)')
for _ in fish_smell:
    print(_)
print(shark)

res_fishes = 0
for i in fish_cnt:
    res_fishes+=sum(i)
print(res_fishes)