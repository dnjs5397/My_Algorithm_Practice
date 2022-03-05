def quick_sort(data):
    if len(data) <= 1:
        return data
    left, right = [], []
    pivot = data[0]
    
    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    # left = [ item for item in data[1:] if pivot > item]
    # right = [ item for item in data[1:] if pivot <= item]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# import random
# data_list = random.sample(range(100), 10)
# print(quick_sort(data_list))

# 시간복잡도
# 병합 정렬과 유사, O(NlogN)
# 단, 최악의 경우 
#   - 맨 처음 pivot이 최댓값이거나 최소값이면 모든 데이터를 비교하는 상황이 발생 -> O(N^2)