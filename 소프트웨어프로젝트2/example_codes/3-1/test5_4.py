data = input("Enter list of sorted numbers (A): ")
numbers = data.split()
aList = [int(i) for i in numbers]
data = input("Enter list of sorted numbers (B): ")
numbers = data.split()
bList = [int(i) for i in numbers]


print("A =", aList)
print("B =", bList)

aPos = 0
bPos = 0
sortnbrs = []

while aPos < len(aList) and bPos < len (bList):
    if aList[aPos] > bList[bPos]:   # bList의 값이 aList값 보다 작을 때
        sortnbrs += [bList[bPos]]   # sortnbrs에 bList값을 더한다.
        bPos += 1                   # bList의 index값을 올린다.
        print(sortnbrs)
    else:
        sortnbrs += [aList[aPos]]   # aList값이 bList값 보다 작을 때 aList의 값을 sortnbrs에 더한다.
        aPos += 1                   # aList의 index값을 올린다.
        print(sortnbrs)


while aPos < len(aList):
    sortnbrs += [aList[aPos]]
    aPos += 1

while bPos < len(bList):
    sortnbrs += [bList[bPos]]
    bPos += 1

print ("Merged = ", sortnbrs)

cList = sorted(aList + bList)
print("By Sort = ", cList)
