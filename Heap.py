# 힙 이란?
# 데이터에서 최대값과 최소값을 빠르게 찾기 위한 이진 트리

# 배열로 최대, 최소값을 찾으면 O(N)이 소요되지만 힙을 이용하면 O(NlogN)

# 최대값을 구하기 위한 Max Heap과 최소값을 구하기 위한 Min Heap으로 분류


class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)        

    def move_down(self, popped_idx):
        left_child_idx = popped_idx * 2
        right_child_idx = popped_idx * 2 + 1
        
        #case1 : 왼쪽 자식 노드도 없을 때
        if left_child_idx >= len(self.heap_array):
            return False
        #case2 : 오른쪽 자식 노드'만' 없을 때
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                return True
            else:
                return False
        #case3 : 자식이 둘다 있을 때
        else:
            if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_idx]:
                        return True
                    else:
                        return False
    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1
        
        while self.move_down(popped_idx):
            left_child_idx = popped_idx * 2
            right_child_idx = popped_idx * 2 + 1
            
            #case2 : 오른쪽 자식 노드'만' 없을 때
            if right_child_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]
            #case3 : 자식이 둘다 있을 때
            else:
                if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                    if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]

                else:
                    if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                        if self.heap_array[popped_idx] < self.heap_array[right_child_idx]:
                            self.heap_array[popped_idx], self.heap_array[right_child_idx] = self.heap_array[right_child_idx], self.heap_array[popped_idx]
        
        return returned_data

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False
        
    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array = list()
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        
        inserted_index = len(self.heap_array) - 1
        
        while self.move_up(inserted_index):
            parent_idx = inserted_index // 2
            self.heap_array[inserted_index], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_index]
            inserted_index = parent_idx
        
        return True

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)