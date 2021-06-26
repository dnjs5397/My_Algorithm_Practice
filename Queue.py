# 라이브러리 사용한 큐

import queue

Array_Queue = list()

Array_Queue.put(1) # push
Array_Queue.qsize() # 큐 크기
Array_Queue.get() # pop


# 직접 구현한 큐

array_Queue = list()

def enqueue(data):
    array_Queue.apppend(data) # 데이터 입력

def dequeue(data):
    data = array_Queue[0] # 먼저 들어간 데이터 
    del array_Queue[0] # 삭제 
    return data # 값 반환

# 우선순위 큐 (Priority Queue)

import queue

list_Queue = queue.PriorityQueue() # 우선순위 큐 선언

list_Queue.put((1, "Korea")) # 함수 괄호 안에 조건 괄호 하나 더 필요 ((우선순위, 데이터))

# Lifo Queue (스택과 동일, Last in first out) <-> 일반적인 큐는 First in first out

import queue

list_queue = queue.LifoQueue()

Array_Queue.put(5) # push
Array_Queue.qsize() # 큐 크기
Array_Queue.get() # pop