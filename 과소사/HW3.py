# HW 3
# 학번 : 20191662
# 이름 : 정민지

# 3-1
x = int(input("곱셈단 시작 정수를 입력하세요: "))
y = int(input("곱셉단 마침 정수를 입력하세요: "))

# 입력받은 y가 x보다 클 경우
if x < y:
    temp = y
    x, y = y, temp

for i in range(x, y+1):
    print('<', i, "단 >")
    for j in range(1, 11):
        print(i, '*', j, '=', i*j)


# 3-2
input_x = int(input("양의 정수를 입력하세요: "))
sum = input_x
count = 1
while (input_x < 0):
    if (input_x == -1):
        break
    input_x = int(input("입력한 수는 양의 정수가 아닙니다! 다시 입력하세요: "))
    sum += input_x
    count += 1
print("입력한 수를 더한 합 : {}, 평균 : {}". format(sum, sum/count))


# 3-3
option = "yes"
while (option == "yes") :
    input_val = input("숫자 또는 문자를 입력하세요: ")
    string_val = []
    int_val = []
    for i in input_val:
        if i.isdigit() == True:
            int_val.append(i)
        else:
            string_val.append(i)

    print(string_val)
    print(int_val)
    option = input("계속 진행하겠습니까?(yes/no) ")

    if option == "no":
        break
