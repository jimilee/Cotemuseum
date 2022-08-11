# gold 2
import sys
import heapq
sys.stdin = open("/home/jml/_workspace/BaekJoon/input.txt", "r")

N = int(sys.stdin.readline())

left = [] # 우선순위 내림차순
right = [] # 오름차순
for i in range(N):
    num = int(sys.stdin.readline())
    print('\n==== {} ===='.format(i))
    if i%2==0: # 짝수일때
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right,(num, num))
    if right and left[0][1] > right[0][1]:
        print('최소값 바꾸기')
        min = heapq.heappop(right)[0]
        max = heapq.heappop(left)[1]
        heapq.heappush(left, (-min, min))
        heapq.heappush(right, (max, max))

    print('---left---')
    for _ in left:
        print(_)
    print('\n---right---')
    for _ in right:
        print(_)
    print(left[0][1])