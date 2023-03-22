import copy
import sys

sys.stdin = open("./input.txt", "r")

N, M = map(int, sys.stdin.readline().split())

samusil = []
dir = {1: [[(0,1)],[(1,0)],[(-1,0)],[(0,-1)]],
       2: [[(0,1),(0,-1)], [(-1,0),(1,0)]],
       3: [[(0,1),(-1,0)], [(-1,0),(0,-1)], [(0,-1),(1,0)], [(1,0),(0,1)]],
       4: [[(0,1),(-1,0),(0,-1)], [(-1,0),(0,-1),(1,0)], [(0,-1),(1,0),(0,1)], [(1,0),(0,1),(-1,0)]],
       5: [[(0,1),(-1,0),(0,-1),(1,0)]]}
cam_loc = {}

def permutations(arr, r): # 순열
    if r == 0:
        return [[]]
    else:
        result = []
        for i in range(len(arr)):
            rest = arr[:i] + arr[i+1:]
            for perm in permutations(rest, r-1):
                result.append([arr[i]] + perm)
        return result

def permut_with_replacement(arr, r): # 중복 순열
    if r == 0:
        return [[]]
    else:
        result = []
        for i in range(len(arr)):
            rest = arr
            for perm in permut_with_replacement(rest, r - 1):
                result.append([arr[i]] + perm)
        return result
def combinations(arr, r):
    if r == 0:
        return [[]]
    else:
        result = []
        for i in range(len(arr)-r+1):
            rest = arr[i+1:]
            for comb in combinations(rest, r-1):
                result.append([arr[i]] + comb)
        return result
def combinations_with_replacement(arr, r):
    if r == 0:
        return [[]]
    else:
        result = []
        for i in range(len(arr)):
            rest = arr[i:]
            for comb in combinations_with_replacement(rest, r-1):
                result.append([arr[i]] + comb)
        return result

cam_cnt =0
for i in range(N):
    f_map = list(map(int, sys.stdin.readline().split()))
    for j, c in enumerate(f_map):
        if c in dir.keys():
            print(f"{c}, ({i},{j})")
            try:
                cam_loc[c].append((i,j))
            except:
                cam_loc[c] = [(i,j)]
            cam_cnt +=1
    samusil.append(f_map)

for i in samusil:
    print(i)
print(cam_loc)
print(3%1, 3%2)

def cam_lot(d):
    tmpsil = copy.deepcopy(samusil)
    i = 0
    print(d)
    for cam_type in cam_loc.keys():
        for cams in cam_loc[cam_type]:
            print("This cam : " , cams,"cam_dirs :", dir[cam_type])
            print("dir idx : ",d[i]%len(dir[cam_type]))
            di = d[i]%len(dir[cam_type])
            move = (dir[cam_type][di])
            print("move : ",move)
            px, py = cams
            for c in move:
                while True:
                    cx, cy = px + c[0], py+c[1]
                    # print(f"{px}, {py} -> {cx}, {cy}")
                    if cx < 0 or cy < 0 or cx >= N or cy >= M or tmpsil[cx][cy] == 6: break
                    if tmpsil[cx][cy] == 0:
                        tmpsil[cx][cy] = -1
                    px, py = cx, cy
            i+=1

    print("="*100)
    for i in tmpsil:
        print(i)
        
# 탐색할 경우의 수
for t in permut_with_replacement(list(range(4)),cam_cnt):
    cam_lot(t)