# 재귀 용법
# Process처리가 Stack구조와 비슷하다
# 파이썬의 경우 재귀 호출의 횟수가 1000회 이하여야 한다
def factorial(num):
    if num > 1:
        print(num)
        return num * factorial(num-1)
    else:
        print(num)
        return num

# print(factorial(10))
#------------------------------------------------

# 예제 1
# 1부터 n까지의 곱 구하기

# def multiple(data):
#     if data <= 1:
#         return 1
#     else:
#         return data* multiple(data-1)
#------------------------------------------------

# 예제 2
# 임의 값으로 만든 리스트의 합

# 풀이 1
# import random
# data = random.sample(range(100), 10)
# def list_sum(list):
#     return sum(list)

# print(list_sum(data))

# 풀이 2
# def list_sum(list):
#     if len(list) == 1:
#         return list[0]
#     else:
#         return list[0] + list_sum(data[1:])
    
# print(list_sum(data))
#------------------------------------------------

# 예제 3
# 회문을 판별할 수 있는 함수
# def recusive(string):
#     if len(string) <= 1:
#         return True
    
#     if string[0] == string[-1]:
#         return recusive(string[1:-1])
#     else:
#         return False
# a = "ABCBA"
# print(recusive(a))

#------------------------------------------------

# 예제 4
# n이 홀수이면 3*n+1 -> 짝수이면 n/2 을 1이 될때까지 진행
# def culculator(N):
#     print(N)
#     if N == 1:
#         return N
    
#     if N % 2 == 1:
#         return culculator(3*N + 1)
#     else:
#         return culculator(N//2)

# print(culculator(3))

#------------------------------------------------
# 예제 5
# 정수 N을 1,2,3의 조합으로 나타내는 방법
def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 3
    
    return func(data-1) + func(data-2) + func(data-3)

print(func(4))