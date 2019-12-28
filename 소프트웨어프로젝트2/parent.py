class Parent:
    house = "young-san"
    def __init__(self):
        self.money = 10000

class Child1(Parent):
    def __init__(self):
        super().__init__()
        pass
class Child2(Parent):
    def __init__(self):
        pass

child1 = Child1()
child2 = Child2()

print(dir(child1))
print(dir(child2))
print(child1.money)
#print(child2.money) --> error
print(child1.house)
print(child2.house)
