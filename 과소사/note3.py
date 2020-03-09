class test:
    def __init__(self, age):
        self.__age = age


    def getAge(self):
        print(self.__age)



if __name__ == '__main__':
    t1 = test(11)
    print(t1.getAge())

