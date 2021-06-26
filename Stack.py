# 파이썬에서는 stack기능이 기본 함수로 있음 append, pop

data_stack = list()

data_stack.append(1) # 입력
data_stack.pop() # 추출

# Stack 직접 구현

Data_stack = list()

def push(data):
    Data_stack.append(data) # 입력

def pop():
    data = Data_stack[-1] # 마지막에 들어간 원소 추출
    del Data_stack[-1] # 삭제
    return data # 반환