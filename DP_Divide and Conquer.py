# 동적 계획법 - Dynamic Programming
# 예) 피보나치 수열
def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)

def fibo_dp(num):
    cache = [0 for i in range(num+1)]
    cache[0] = 0
    cache[1] = 1
    
    for i in range(2, num+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[num]