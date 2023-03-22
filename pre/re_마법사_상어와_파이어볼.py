import copy
import sys

sys.stdin = open("./input.txt", "r")

directions = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
N, M, K = map(int, sys.stdin.readline().split())

boards = {}
fireballs = {}
last_id = 0
for i in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireballs[i] = [r,c,m,s,d]
    last_id = i+1
    try: boards[(r,c)].append(i)
    except: boards[(r,c)] = [i]

def move_fireballs(fireballs):
    tmp_boards = {}
    tmp_fireballs = {}
    for id,f in fireballs.items():
        r,c,m,s,d = f
        print(id, '번째 파이어볼...', r,c, m, s, d)
        sx, sy = (directions[d][1] * s), (directions[d][0] * s)
        nx, ny = (r + sx + N) % N, (c + sy + N) % N
        x,y = nx, ny

        print(r, c, '->', x, y)
        try: tmp_boards[(x,y)].append(id)
        except: tmp_boards[(x,y)] = [id]
        tmp_fireballs[id] = [x,y,m,s,d]
    return tmp_boards, tmp_fireballs

result_dt, result_df = [0,2,4,6], [1,3,5,7]
def asemble_fireballs(boards, fireballs, last_id):
    tmp_boards = copy.deepcopy(boards)
    tmp_fireballs = copy.deepcopy(fireballs)
    for loc, fbs in boards.items():
        print(fbs)
        x, y = loc
        if len(fbs)>1 : # 볼이 두개이상일 때
            tmp_boards[(x,y)].clear()
            print('==after clear, 파이어볼 합치기 시작. === ', x, y)
            print(tmp_boards)
            total_w = 0 # 총 질량
            total_s = 0 # 총 속력
            check_d = -1 # 방향 체크.  0 = 짝, 1 = 홀
            is_D_flag = True
            print(fireballs)
            for f in fbs:
                r, c, m, s, d = fireballs.pop(f)
                tmp_fireballs.pop(f)
                total_w += m
                total_s += s
                if check_d == -1:
                    check_d = d%2
                elif check_d != d%2:
                    is_D_flag = False
            result_w = int(total_w/5)
            result_s = int(total_s/len(fbs))
            print(result_s, result_w)
            if result_w > 0: # 파이어볼이 소멸 되지 않았을 때.
                for i in range(4):
                    if is_D_flag: # 모두 짝 or 홀
                        tmp_fireballs[last_id] = [x, y, result_w, result_s, result_dt[i]]
                        tmp_boards[(x,y)].append(last_id)
                        last_id+=1
                    else: # 모두 짝 or 홀
                        tmp_fireballs[last_id] = [x, y, result_w, result_s, result_df[i]]
                        tmp_boards[(x,y)].append(last_id)
                        last_id+=1
        print(tmp_fireballs)
        print('tmp_board: ',tmp_boards)
        print('board: ', boards)
    return tmp_boards, tmp_fireballs, last_id

for turn in range(K):
    print('==============================', turn,'==============================')
    print(boards)
    print(fireballs)
    boards, fireballs = move_fireballs(fireballs)
    boards, fireballs, last_id = asemble_fireballs(boards,fireballs, last_id)

result = 0
for f in fireballs.values():
    _,_,m,_,_ = f
    result+=m
print(result)


