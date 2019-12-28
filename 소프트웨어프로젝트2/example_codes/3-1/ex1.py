# 최솟값 찾기

# 1
data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]     # 문자를 숫자로 바꿈
minval = 99999999
for val in numbers:
    if (minval > val):
        minval = val
print("Minimum value:", minval)
# 한계점 : 모든 numbers에 있는 수가 minval보다 크다면 최솟값을 찾을 수 없다.

# 2
minval = numbers[0]
for val in numbers:
    if (minval > val):
        minval = val
print("Minimum value2:", minval)
# 1의 한계점 보완
# 한계점 : numbers의 원소가 0개인 경우 에러 발생

# 3 제일 작은 숫자의 index값 찾기
minval = numbers[0]
minidx = 0
for i in range(1, len(numbers)):
    if (minval > numbers[i]):
        minval = numbers[i]
        minidx = i
print("Min Val:", minval, "Min Index:", minidx)

maxval = numbers[0]
maxidx = 0
for i in range(1, len(numbers)):
    if (maxval < numbers[i]):
        maxval = numbers[i]
        maxidx = i
print("Max Val:", maxval, "Max Index:", maxidx)

# 합계, 평균 구하기
currentsum = 0
for i in numbers:
    currentsum += i

print("Sum value:", currentsum)
print("Average value:", currentsum / len(numbers))

# 내장함수로 구하기
print("Min,Built-in:", min(numbers))
print("Max,Built-in:", max(numbers))
print("Sum,Built-in:", sum(numbers))

scoredb = [ {'Name':'Lee', 'Score':30},
    {'Name':'Kim', 'Score':40},
    {'Name':'Park', 'Score':50},
    {'Name':'Choi', 'Score':90} ]

# person은 x와 같은 의미이다. score에 들어있는 값 중 하나의 사전값
# 이름과 성적을 key값을 가지고 있는 것을 person이라고 정의하고 그 중에서 Score값을 기준으로 최소값, 최대값을 찾는다.
# lamda : 한 줄 함수 뒤에는 파라미터, 함수의 return값이 들어간다.
print("Min:", min(scoredb, key=lambda person: person['Score']))
print("Max:", max(scoredb, key=lambda person: person['Score']))
