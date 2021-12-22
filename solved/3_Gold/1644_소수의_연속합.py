import sys
import math
from collections import deque

def make_prime(n): #에라토스테네스의 체
    result = []
    arr = [True] * (n + 1)

    for i in range(2, int(math.sqrt(n) + 1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:
                arr[i * j] = False
                j += 1

    for i in range(2, len(arr)):
        if arr[i] == True:
            result.append(i)
    return result

sys.stdin = open("../../input.txt", "r")

n = int(sys.stdin.readline())
prime_list = make_prime(n+1)
match_cnt = 0
print(prime_list)
for i in range(len(prime_list)): # 리스트 사이즈로 순환
    tmp = 0 # 임시 숫자 저장
    t = i
    print('시작 숫자 : ', t)
    while True:
        tmp += prime_list[t]
        print('더하기 : ', prime_list[t], '현재 숫자 :', tmp)

        if tmp > n: # 지나갔을때
            break
        elif tmp == n: # 타겟과 일치할때
            print(t, 'tmp : ', tmp, '목표 넘버 : ', n)
            match_cnt +=1
            break

        t+=1
        if t >= len(prime_list): break

print(match_cnt)
