"""
Name: {chalita sahnguanchao}
ID: {364211760023}
Group: {MIT211}
"""

# Encapsulation

class Student:
    def__inif__(self,name,age):
    self.name = name
    self.age = age

    def display_info(self):
        print(f'Name: {sellf.name} Age: {self.age}')

# create object of Student
std = Student('Chalita Sahnguanchao','22')
print(std.name) # direct access
print(std.age) # 22
std.display_info()

std.age = 40
print(std.age) # 40
std.age = -100
print(std.age)
std.display_info()