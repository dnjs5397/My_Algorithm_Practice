# 최적의 해에 가까운 값을 구하기 위해 사용됨
# 매 순간 최적이라고 생각되는 경우를 선택

# sort() 또는 sorted를 사용해 선택지를 미리 정렬해놓고 순차적으로 처리

### 동전 문제
coin_list = [500, 100, 50, 1]

def min_coin_count(value, coin_list):
    total_coint_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coint_count += coin_num
        value -= coin_num*coin
        details.append([coin, coin_num])
        if (value <= 0):
            break
        
        
    print(total_coint_count, details)
###

### 부분 배낭 문제
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
data_list = sorted(data_list, key=lambda x: x[1]/ x[0], reverse = True)

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1]/ x[0], reverse = True)
    total_value = 0
    details = list()
    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    print(total_value, details)
###            


# 그리디 알고리즘의 한계
# - 탐욕 알고리즘은 근사치 추정에 활용
# - 반드시 최적의 해를 구할 수 있는 것은 아님
# - 예시로는 트리 구조에서 최소 합 구하기