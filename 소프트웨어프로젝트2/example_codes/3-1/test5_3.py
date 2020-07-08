# 선형탐색과 이진탐색의 성능 비교

import time
import random

def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def binsearch(nbrs, target):
    lower = 0
    upper = len(nbrs) - 1
    idx = -1
    while (lower <= upper):
        middle = int((lower + upper) // 2)
        if nbrs[middle] == target :
            idx = middle
            break
        elif nbrs[middle] < target :
            lower = middle + 1
        else:
            upper = middle - 1
    return idx



numofnbrs = int(input("Enter a number: "))      # 검사하려는 숫자의 개수
numbers = []                                    # 검사하려는 리스트
for i in range(numofnbrs):                      # 리스트에 수를 랜덤으로 입력받은 개수만큼 담는다.
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))  # 타겟의 개수
targets = []                                                # 타겟의 리스트
for i in range(numoftargets):                               # 타겟리스트에 입력받은 개수만큼의 타겟을 담는다.
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search
cnt = 0
for target in targets:
    idx = binsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("Binary Search %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("Sequential Search %d: not found %d time %.6f" % (numoftargets, cnt, ts))
