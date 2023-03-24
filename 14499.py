import copy
import sys

sys.stdin = open("./input.txt", "r")

N, M, x,y,k = map(int, sys.stdin.readline().split())

print(N, M, x,y, k)
maps = [list(map(int, sys.stdin.readline().split())) 
        for i in range(N)]
orders = list(map(int, sys.stdin.readline().split()))
for i in maps:
  print(i)
print(orders)
            # 바닥면 :  동, 서, 북, 남, 윗면
dice_val = [0,0,0,0,0,0]
dice_stat = { 6 : [3, 4, 2, 5, 1],
              5 : [3, 4, 6, 1, 2],
              4 : [6, 1, 2, 5, 3],
              3 : [1, 6, 2, 5, 4],
              2 : [3, 4, 1, 6, 5],
              1 : [3, 4, 5, 2, 6]}

tmpmaps = copy.deepcopy(maps)
dx, dy = (0, 0, -1, 1),(1, -1, 0, 0)
cur_dice = 6

px, py = x,y
for d in orders:
  print("="*30, d, "="*30)
  cx, cy = px + dx[d-1], py + dy[d-1]
  if cx < 0 or cy < 0 or cx > N or cy > M: continue
  if tmpmaps[cx][cy] == 0:
    tmpmaps[cx][cy] = dice_stat[cur_dice][d-1]
    cur_dice = dice_stat[cur_dice][d-1]
  else:
    dice_val[dice_stat[cur_dice][d-1]-1] = tmpmaps[cx][cy]
    tmpmaps[cx][cy] = 0
    cur_dice = dice_stat[cur_dice][d-1] # 현재 밑면
  px, py = cx, cy
  for i in tmpmaps:
    print(i)
  print("현재 윗면 : ", dice_stat[cur_dice][4], " 밑면,",cur_dice)
  print(dice_val[dice_stat[cur_dice][4]-1])
  print(dice_val)


  
