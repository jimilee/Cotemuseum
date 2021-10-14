from collections import deque
# O(1) 로 minimum 구하기
class minimum_Stack():
    def __init__(self):
        self.Stack = [] #파이썬은 리스트를 스택으로 사용
    def push(self, element): # 스택 push
        if not self.Stack:
            self.Stack.append([element, element])
        else: # 현재 스택의 최솟값(top.second)과 입력값을 비교하여 추가시킴.
            self.Stack.append([element, min(element, self.Stack[-1][1])])
    def pop(self):
        return self.Stack.pop() #스택 pop
    def pop_minimum(self):
        return self.Stack[-1][1] #스택 pop - 최솟값

class minimum_Queue():
    def __init__(self):
        self.Queue = deque() #파이썬 collections.deque - 내부적으로 linked list를 사용함.
    def push(self, element): # 큐 push
        if not self.Queue:
            self.Queue.appendleft(element)
            self.Queue.append(element)
        else: # 현재 큐의 최솟값과 입력값을 비교하여 끝 인덱스에 추가시킴.
            min_value = self.Queue.pop()
            if min_value < element: #최소값 갱신
                self.Queue.append(element)
                self.Queue.append(min_value)
            else:
                self.Queue.append(element)
                self.Queue.append(element)
    def pop(self):
        return self.Queue.popleft() #큐 pop
    def pop_minimum(self):
        return self.Queue.pop() #큐 pop - 최솟값

q = minimum_Queue()
q.push(5)
q.push(4)
q.push(8)
print(q.pop_minimum())