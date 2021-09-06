
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
results = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
def solution(lottos, win_nums):
    answer = []
    total = lottos + win_nums
    total.sort()
    win_cnt, zero_cnt = 0,0
    tmp = -1
    for i in range(len(total)):
        if total[i] == 0:
            zero_cnt += 1
        elif tmp == total[i]:
            win_cnt += 1
            i +=2
        else: tmp = total[i]
    answer.append(results[win_cnt+zero_cnt])
    answer.append(results[win_cnt])
    print(answer)
solution(lottos, win_nums)