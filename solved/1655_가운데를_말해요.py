import sys
import heapq

sys.stdin = open("../input.txt", "r")

x = int(sys.stdin.readline())#x

left = []
right = []
for i in range(x):
    num = int(sys.stdin.readline())

    if len(left)==len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right,(num, num))
    if right and left[0][1] > right[0][0]:
        min = heapq.heappop(right)[0]
        max = heapq.heappop(left)[1]
        heapq.heappush(left, (-min, min))
        heapq.heappush(right, (max, max))
    print(left[0][1])
