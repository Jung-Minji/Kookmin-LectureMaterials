def solution(myList):
    answer = 0
    d = {}
    for i in range(len(myList)):
        if myList[i] not in d.keys():
            d[myList[i]] = 1
        else:
            d[myList[i]] += 1
    lst = sorted(d, key = lambda x:d[x])

    if len(myList) <= 1:
        return -1
    if len(myList) == 1:
        return myList[0]

    item_lst = d.values()
    max_num = max(item_lst)
    count = 0


    # max_num이 두 개 이상일 경우 -1 리턴
    for i in item_lst:
        if i == max_num:
            count += 1

    if count > 1:
        return -1

    # 모든 max_num이 같을 경우 -1리턴
    key_lst = []
    for i in d.keys():
        key_lst.append(i)

    if lst == key_lst:
        return -1

    return lst[-1]



if __name__ == '__main__':
    print(solution([1,2,3,4]))
    print(solution([2,2,2,2,2]))
    print(solution([2]))