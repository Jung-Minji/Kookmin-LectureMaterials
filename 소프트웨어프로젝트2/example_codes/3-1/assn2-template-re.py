import time
import random

# 선형 탐색
def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

# 이진탐색 - 재귀적 구현
def recbinsearch(L, l, m, u, target):
    if target not in L:
        return -1
    else:
        if L[m] == target:
            return m

        elif L[m] > target:
            u = m - 1
            return recbinsearch(L, l, int((l + u) // 2), u, target)

        else:
            l = m + 1
            return recbinsearch(L, l, int((l + u) // 2), u, target)


numofnbrs = int(input("Enter a number: "))  # 검사할 리스트의 개수 입력
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))  # target의 개수 입력
targets = []    #target 리스트
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers)//2, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))