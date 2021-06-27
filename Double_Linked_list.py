class Node:
    def __init__ (self, data, prev = None, next = None):
        self.prev = prev
        self.next = next
        self.data = data

class NodeManagement:
    def __init__ (self, data): # 노드 생성
        self.head = Node(data)
        self.tail = self.head
        
    def insert(self, data):  # 데이터 삽입
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data) # 새로운 노드 생성
            node.next = new  # 마지막 노드의 다음 -> 새로운 노드
            new.prev = node  # 새로운 노드의 이전 -> 마지막 노드
            self.tail = new  # tail을 새로운 노드로 변경

    def search_insert(self, dest, data):
        node = self.head
        while node.next:
            if (node.next.data == dest):
                new = Node(data)
                new.next = node.next
                node.next.prev = new
                node.next = new
                new.prev = node
                return
            else:
                node = node.next
        print("해당 값을 가진 노드가 없음")



    def print_all(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

arr = NodeManagement(0)
for i in range(1,10):
    arr.insert(i)

arr.search_insert(2, 1.5)

arr.print_all()
