# 선형 탐색 - 특정한 수 찾기
data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]

def seqsearch(nbrs, tgt):
    for i in range(0, len(nbrs)):
        if (tgt == nbrs[i]):
            return i
    return -1

target = int(input("Enter the number to find: "))   # 주의! 입력받는 타켓값을 int로 형변환한다.
idx = seqsearch(numbers, target)
print("Target:", target, "Index:", seqsearch(numbers, target))

# 리스트의 원소가 단순한 숫자가 아닌 경우의 예
scoredb = [ {'Name':'Lee', 'Score':30},
    {'Name':'Kim', 'Score':40},
    {'Name':'Park', 'Score':50},
    {'Name':'Choi', 'Score':90} ]

def findScoreDB(scdb, keyname):
    for i in range(0, len(scdb)):
        if (keyname == scdb[i]['Name']):
            return i
    return -1

name = input("Enter name: ")
idx = findScoreDB(scoredb, name)
if idx >= 0:
    print(scoredb[idx])
else:
    print("No Such Name")

# 참고
persons = [p for p in scoredb if p["Name"] == name]

persons1 = list(filter(lambda x: x["Name"] == name, scoredb))
