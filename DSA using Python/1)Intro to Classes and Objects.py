# Intro to Classes and Objects
class Employee:
    def __init__(self, empid = None, name = None, salary =  None ):
        self.empid = empid
        self.name = name
        self.salary = salary

    def setEmpid(self, empid):
        self.empid=empid

    def setName(self, name):
        self.name=name

    def setSalary(self, salary):
        self.salary=salary

    def getEmpid(self):
        return self.empid

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

emp1=Employee()
e2=Employee(102,'Business', 50000)
emp1.setName('Ajay')
emp1.setEmpid(101)
emp1.setSalary(25000)
print(emp1.getName())
print(emp1.getSalary())
print(emp1.getEmpid())
print(e2.getEmpid(), e2.getName(), e2.getSalary())


# Built-in function operations on a list
# demoList = [23, 56, 74, 34, 10, 78]
# print(sorted(demoList))
#
# # Array from numpy module
# from numpy import *
# a= array([12,23,34,64])
# print(a)