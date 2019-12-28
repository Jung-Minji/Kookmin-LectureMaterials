from person import Person
p = Person('James', 'Developer', 100)
print(p)
print(p.name)
print(p.job)
print(p.pay)
p.job = 'Manager'
print(p.job)

# bob = Person("Bob Smith")
# sue = Person("Sue Jones", job = "dev", pay = 1000000)
#
# bob.name.split()[-1]
#
# sue.pay *= 1.1
# print(sue.pay)

from manager import Manager

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    print("--------------")
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", "dev", 100000)
    tom = Manager("Tom Jones", "mgr", 50000)
    #
    # development = Department(bob, sue)
    # development.addMember(tom)
    # development.giveRaises(.10)
    # development.showAll()

