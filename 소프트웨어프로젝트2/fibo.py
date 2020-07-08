import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

def iterfibo(n):
    fibo_lst = [0,1]
    for i in range(2,n+1):
        fibo_lst.append(fibo_lst[i-2] + fibo_lst[i-1])

    return fibo_lst[n]


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time = %.6f" %(nbr, fibonumber, ts))

    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time = %.6f" %(nbr, fibonumber, ts))


# 선형 탐색과 이진 탐색의 장단점
# 이진 탐색 : 데이터를 검색하는 방법이 간단하지만, 데이터의 개수만큼 확인하기 때문에 검색 성능이 데이터의 양에 따라 좌우된다.
# 선형 탐색 : 미리 정렬되어 있는 데이터를 절반씩 잘라서 검색하기 때문에 이진 탐색에 비해 성능이 좋아 검색 속도가 빠르다.
#           트리 구조를 기반으로 하기 때문에 공간의 효율성면에서도 선형 탐색에 비해 좋다.