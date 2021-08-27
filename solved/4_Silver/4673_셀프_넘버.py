
selfNum = [True] * 10000
def isSelfNum(n):
    N = n
    if len(str(n)) < 2:
        selfNum[n+n] = False
    else:
        for num in list(str(n)):
            N += int(num)
        if N < 10000:
            selfNum[N] = False

for i in range(1, 10000):
    isSelfNum(i)

for i in range(1, 10000):
    if selfNum[i]:
        print(i)