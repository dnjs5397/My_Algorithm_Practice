# 사용할 공간을 미리 할당해줘야 하는 list의 불편함을 해소하고자
# Linked List 이용 (메모리 자동할당)
# 장점 : 데이터 공간 미리 할당 안해도 됨
# 단점 : 데이터 탐색에 시간이 오래걸림(비효율적) / 중간 데이터 삭제 시 추가 연결작업 필요 / 

'''class Node:
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


# -------------------------- Linked list 데이터 출력 (검색)

node = head
while node.next: # 마지막 노드 전까지 데이터 출력
    print(node.data)
    node = node.next
print(node.data) # 마지막 노드도 출력


# -------------------------- Linked list 노드들 사이에 데이터 삽입
node3 = Node(1.5) # node3 을 노드 사이에 삽입할 것임

node = head
search = True
while search:
    if (node.data) == 1: # 1다음에 1.5 삽입
        search = False
    else:
        node = node.next

node_next = node.next # 찾은 노드의 다음 노드 주소 저장
node.next = node3
node3.next = node_next'''

# ---------------------------- 위 모든 기능을 클래스 내에 구현한 Linked list 만들기

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class NodeManagement:
    def __init__(self, data):
        self.head = Node(data) # 노드를 새로 생성할때 head를 한번에 지정
    
    def add(self,data):
        if self.head == None: # head 값이 없다면 새로 추가한 값이 head
            self.head = Node(data)
        else:
            node = self.head # head 값이 존재한다면 head에서 마지막 노드까지 간 후 추가해줘야함
            while node.next:
                node = node.next
            node.next = Node(data)

    def delete(self, data): # 1. head 삭제 2. 마지막 노드 삭제 3. 중간 노드 삭제
        if self.head == None:
            print("해당 값을 가진 노드가 없음.")
            return
        if self.head.data == data: # head 삭제
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head # 중간 노드 삭제
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    break # 삭제하고 탈출
                else:
                    node = node.next
                    if (node.next == None):
                        print("해당 값을 가진 노드가 없음.") # 루프 다 돌았는데 찾는 값 없으면 출력


    def print_all(self): # 출력 함수
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search(self, data): # 탐색 함수
        node = self.head
        while node:
            if (node.data == data):
                print(node.data)
                return
            else:
                node = node.next
        print("해당 값을 가진 노드가 없음.")
