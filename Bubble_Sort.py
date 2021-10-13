#import random

#list = random.sample(range(100), 10)
list = list(map(int, input().split()))
leng = len(list)
turn = 0
for i in range(leng-1):
    for j in range(leng - 1 - i):  # 반복문이 두개 -> O(n^2) / 정렬돼있는 상태라면 O(n)
        if (list[j] > list[j+1]):
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
            turn += 1
    if turn == 0:
        print("Perfect Array")
        print(list)
        exit(0)

print(list)