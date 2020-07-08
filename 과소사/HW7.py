# HW 7-1 : 학생에 대한 클래스 만들기
# 학번 : 20191662
# 이름 : 정민지

class Student:

    count = 0

    def __init__(self, name=None, phone_number=None,  age=0, id=0, hobby=None):
        self.__name = name
        self.__age = age
        self.__phoneNumber = phone_number
        self.__hobby = hobby
        self.__id = id
        Student.count += 1

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def getphoneNumber(self):
        return self.__phoneNumber

    def getHobby(self):
        return self.__hobby

    def getId(self):
        return self.__id

    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def setHobby(self, hobby):
        self.__hobby = hobby

    def setId(self, id):
        self.__id = id

    def __add__(self, other):
        return self.getAge() + other.getAge()

    def getStudentCount():
        return Student.count

if __name__ == '__main__':
    student1 = Student("김이름", 20, "01000000000", "야구")
    student2 = Student("이이름", 21, "01022222222", "축구")
    print(student1.getAge())
    print(student1.getName())
    print(student1.getHobby())
    print(student1 + student2)


