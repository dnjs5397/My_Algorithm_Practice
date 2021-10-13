# 주어진 데이터 중 최소값을 찾음
# 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
# 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

list = [2,7,5,8,6,1]

for i in range( len(list) -1 ):
    index = i
    for j in range( i+1, len(list) ):
        if (list[index] > list[j]):
            index = j

    list[index], list[i] = list[i], list[index]

print(list)