import sys

sys.stdin = open("/home/jml/_workspace/BaekJoon/input.txt", "r")

N, K = map(int, sys.stdin.readline().split())# N 물품의 수  # K 준서가 버틸수 있는 무게
print(N, K)
inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(inputs)

max_val = 0
in_bag = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N):
    weight = int(inputs[i][0])
    value = int(inputs[i][1])
    for j in range(1, K+1):
        if weight > j:
            in_bag[i+1][j] = in_bag[i][j]
        else:
            in_bag[i+1][j] = max(value + in_bag[i][j-weight], in_bag[i][j])

print(in_bag[N][K])
# print(in_bag)


# import sys
# sys.stdin = open("/home/jml/_workspace/BaekJoon/input.txt", "r")
# inputs = []
# while True:
#     try:
#         x, y = map(int, sys.stdin.readline().split())
#         inputs.append([x,y])
#     except:
#         break
# N = inputs[0][0] #물품의 수
# K = inputs[0][1] #준서가 버틸수 있는 무게
# max_val = 0
# in_bag = [[0 for _ in range(K+1)] for _ in range(N+1)]
# for i in range(1, N+1):
#     weight = int(inputs[i][0])
#     value = int(inputs[i][1])
#     for j in range(1, K+1):
#         if weight > j:
#             in_bag[i][j] = in_bag[i-1][j]
#         else:
#             in_bag[i][j] = max(value + in_bag[i-1][j-weight], in_bag[i-1][j])
#
# print(in_bag)
