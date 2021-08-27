input = '4 7\n6 13\n4 8\n3 6\n5 12'

def minge():
    n, m = map(int, input().split())
    tmp_list = [list(map(int, input().split())) for _ in range(n)]
    t_max = 0
    for i in range(n):
        if tmp_list[i][0] <= m:
            if t_max < tmp_list[i][1]:
                t_max = tmp_list[i][1]
        for j in range(i + 1, n):
            if tmp_list[i][0] + tmp_list[j][0] <= m:
                tmp = tmp_list[i][1] + tmp_list[j][1]
                if t_max < tmp:
                    t_max = tmp
    print(t_max)

inputs = input.split('\n')
print(inputs)
N = int(inputs[0].split(' ')[0]) #물품의 수
K = int(inputs[0].split(' ')[1]) #준서가 버틸수 있는 무게

print(N, K)
max_val = 0
cur_weight = 0
in_bag = [[0 for _ in range(K)] for _ in range(N)]

for i in range(1, N):
    weight = int(inputs[i][0])
    value = int(inputs[i][1])
    for j in range(1, K):
        if weight > j:
            in_bag[i][j] = in_bag[i-1][j]
        else:
            in_bag[i][j] = max(value + in_bag[i-1][j-weight], in_bag[i-1][j])
        print('%2d'%in_bag[i][j], end=' ')
        if in_bag[i][j]> max_val:
            max_val = in_bag[i][j]
    print()

print('max_val : ',max_val)

