# HW6 : 친구 연락처 관리 프로그램 만들기
# 학번 : 20191662
# 이름 : 정민지

from Lecture import HW7

def appendFile(name, phoneNumber, age, id, hobby):
    file = open("phoneNumber.txt", "a")
    getData()
    num_dic[name] = [phoneNumber, age, id, hobby]
    file.write('\n' + name + "\t" + phoneNumber + '\t' + age + '\t' + id + '\t' + hobby)
    student = HW7.Student(name, phoneNumber, age, id, hobby)
    file.close()
    getData()
    reData()


def readFile():
    file = open("phoneNumber.txt", 'r')
    reData()
    read = file.read()
    print(read)
    file.close()

def removeNumber(removeName):
    file = open("phoneNumber.txt", "a")
    getData()
    if removeName in num_dic.keys():
        num_dic.pop(removeName)
    HW7.Student.count -= 1
    reData()
    file.close()

def reName(old_name, new_name):
    file = open("phoneNumber.txt", "a")
    getData()
    if old_name in num_dic.keys():
        val = num_dic[old_name]
        num_dic.pop(old_name)
        num_dic[new_name] = val
    reData()
    file.close()


def getData():
    file = open("phoneNumber.txt", "r")
    for line in file:
        line = line.rstrip()
        word_lst = line.split('\t')
        if word_lst == ['']:
            continue
        num_dic[word_lst[0]] = [word_lst[1], word_lst[2], word_lst[3], word_lst[4]]
    file.close()

def reData():
    file = open("phoneNumber.txt", "w")
    for key, val in num_dic.items():
        file.write('\n' + key + "\t" + val[0] + '\t' + val[1] + '\t' + val[2] + '\t' + val[3])
    file.close()

def addAge():
    getData()
    age = 0
    for key in num_dic.keys():
        age += int(num_dic[key][1])
    print("총 친구들의 나이를 더한 값은 " + str(age) + "입니다.")


if __name__ == '__main__':
    global num_dic
    num_dic = {}
    getData()
    reData()
    while (True):
        print("-------menu-------")
        print("1. 연락처 입력하기")
        print("2. 연락처 읽기")
        print("3. 연락처 삭제하기")
        print("4. 이름 수정하기")
        print("5. 친구들 나이 더하기")
        print("6. 총 인원 수 출력하기")
        print("7. 종료하기")
        status = input("메뉴를 선택하세요(1 or 2 or 3...)")
        if status == '1':
            print("친구의 이름과 연락처를 입력하세요")
            s = True
            while s:
                name = input("친구의 이름: ")
                number = input("친구의 연락처: ")
                age = input("친구의 나이: ")
                id = input("친구의 학번: ")
                hobby = input("친구의 취미: ")
                if not (name == "" and number is None):
                    appendFile(name, number, age, id, hobby)
                s = input("연락처 입력을 종료하시겠습니까?(y/n)")
                if s == 'y':
                    s = False

        elif status == '2':
            readFile()

        elif status == '3':
            removeName = input("삭제할 친구의 이름을 입력하세요: ")
            removeNumber(removeName)

        elif status == '4':
            print(num_dic)
            old_name = input("잘못 입력한 이름을 입력하세요: ")
            new_name = input("수정할 이름을 입력하세요: ")
            reName(old_name, new_name)

        elif status == '5':
            addAge()

        elif status == '6':
            print("현재 입력된 총 인원수는 %d 입니다" % len(num_dic))
            # getStudentCount()을 사용하면 나갔다 다시 들어왔을 때 이미 만들어진 학생의 수는 카운트되지 않기 때문에
            # num_dic의 길이를 사용하였다.

        elif status == '7':
            break

        else:
            status = input("다시 메뉴를 선택하세요(1 or 2 or 3...)")





