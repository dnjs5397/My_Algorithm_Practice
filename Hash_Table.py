# Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 매우 빨라짐 (배열 완전탐색에 비해)
# 파이썬에서는 해쉬 별도 구현 필요없음 - 딕셔너리(Dictionary) 타입을 이용하면 됨
# 보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용

hash_table = list([0 for i in range(10)])

# Division 방법 (나누기를 통한 나머지 값 = 키)
def hash_func(key):
    return key % 5

# 데이터 저장
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'


#print(hash_func(ord(data1[0])), hash_func(ord(data2[0])), hash_func(ord(data3[0])))  ### ord(): 문자의 ASCII코드 리턴 / 키 계산

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data(data1, '014928370711591')
storage_data(data2, '014643634183591')
storage_data(data3, '014922462262591')

# 데이터 출력
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    print(hash_table[hash_address])
    return