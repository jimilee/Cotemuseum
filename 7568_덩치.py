import sys
sys.stdin = open("/home/jml/_workspace/BaekJoon/input.txt", "r")

N = int(sys.stdin.readline())

datas = []
counts = [1 for _ in range(N)]
for idx in range(N):
    w, h = map(int, sys.stdin.readline().split()) # 현재덩치
    if idx == 0:
        datas.append([w, h])
        continue
    for jdx, j in enumerate(datas):
        jw, jh = j
        print(f'{jw}, {jh} <-> {w},{h}')
        if w < jw and h < jh: # 현재 덩치보다 더 큰덩치
            print('더 큰덩치')
            counts[idx] += 1
        elif w > jw and h > jh: # 현재 덩치보다 더 작은덩치
            print('더 작은덩치')
            counts[jdx] += 1
    datas.append([w, h])

print(' '.join(map(str, counts)))

