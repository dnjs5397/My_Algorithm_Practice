# 사용할 공간을 미리 할당해줘야 하는 list의 불편함을 해소하고자
# Linked List 이용 (메모리 자동할당)


# ----------------------- Node 클래스만 구현하고 선언과 연결은 직접

class Node:  # 선언 1
    def __init__(self, data):
        self.data = data
        self.next = None

class Node: # 선언 2 == 선언 1
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

# ------------------------- Node 클래스 내에서 선언과 연결 모두

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head # head 노드의 주소 할당
    while node.next: # next의 주소가 없을때까지 계속 이동 -> 마지막 노드까지 이동
        node = node.next # 탈출하면 마지막 노드
    node.next = Node(data) # 마지막 노드 뒤에 새 노드 생성

node1 = Node(1)
head = node1
for i in range(1,10): # for i in range (a,b) -> a부터 시작해서 b개 -> a부터 b-1까지
    add(i)


### Linked list 데이터 출력 (검색) ###

node = head
while node.next: # 마지막 노드 전까지 데이터 출력
    print(node.data)
    node = node.next
print(node.data) # 마지막 노드도 출력