# Syntax
# print("hellow python") 


# if 5 > 2:
    # print("five is greater then 2")


# str, int, float 

# python has 8 kinds of data types

# text type - string 
# numeric type - int, float, complext
# sequence type - tuple, list, range
# set type - set
# boolean type - true false, bool
# maping type - dict
# none type - none
# binary type - binary, binarmaping

# String====================================
# myVar = 'hellow world'
# print(myVar[2:5])
# print(myVar[:2])
# print(myVar.upper())

# print(myVar.strip())
# modify - replace, stripe,split,upper, lower
# concatenation - a + b
# escape charachter - \ \\ \n 

# string method
# capialize()
# casefold - convert string into lower case
# center - returns a centered string
# count();
# encode(): 
# endswith()
# expandtabs():
# find():
# format():
# format_map():
# index();
# isdigit();
# islower();
# isspace();
# istitle();
# issupper();
# isstrip();
# partition():
# replace():
# rfind();
# rindex():
# startwith();
# swapcase():
# title():
# translate():
# upper();


# Boolean Methods
# > == <
# Operators
# +, -, *, /,%, **, //


# List =====================
# a = ['apple', 'banana', 'cherry', 'apple', 'something else']
# a[1]
# a[1:5]
# a[:5]
# a[2:]

# if 'apple' in a:
#     print('yes apple has')

# # change items 
# a[1] = 'katol'
# a.append('orange')
# a.append(2,'komola')


# x = [1,4,5,5,67]
# y = (4,6,6,6,7,8)
# x.extend(y)
# print(x)

# # To remove list items
# remove,
# pop() - remove last items ('items')
# del listname[4]
# del listname
# a.clear();

# Loop throug in Lists ==========================
# a = [3,5,6,67,7,8,8,99]
# for x in a:
#     print(a)


# for x in range(len(x)):
#     print(a)


# # copy lists
# a.copy();
# mylsist = list(a);

# b = [4,6778,9,000,33]
# a.extend(b)
# for i in b:
#     a.append(i)

# List methods =============================

# append();
# clear();
# copy();
# count();
# extend();
# index();
# insert();
# pop();
# remove();
# reverse();
# sort();

# tuple = unchangable (immutable )
# it's also access item by index

# to update tuple
# x = ("hellow", "world")
# (a,b) = x
# print(a,b)
# y = list(x);
# y[1] = 'galaxy'

# print(y)
# append 
# can be loop as well
# can be tuple multpley

# Sets = {}
# mysets = {"apple", "microsoft", "someth"}
# unchangalbe but we can remove or add new items duplicatte now allowed

# Python dictionary 
# thisdic = {
#     "brand":"apple"
# }

# # Dictionary Methods =======================
# clear();
# copy();
# formkeys();
# get();
# items();
# keys();
# pop();
# poptiem();
# setdefault();
# update();
# values();

# Python condition 
# a == b
# !=
# <
# >
# <=
# >=
# if b > a :
#     print("hellow")
# else :
#     print("hellow wot")

# i = 0
# while i < 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1


# Loop ================================
# for loop
# for x in a:
#     print (x)


# loop can be possible in string

# for x in "banner":
#     print (x)
# function =========================================
# def myfunction():
#     print("hellow ")

# class ========================

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p = Person('ujjal', 30)
# print(p.name +' ' + str(p.age))

# Python modules
# NumPy
# Pandas
# Scipy
# django

# OOP - 
# 1. Class & Object
# 2. Inheritance
# 3. Abstraction
# 4. Encapsulation
# 5. Polymorphism
# Python Class ===================================

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"{self.name} ({self.age})"
    
    def myfunc(self, location):
        print("Hellow world", self.age, ' ', location)


a = MyClass('ujjal', 20)
# print(a.name)
# print(a)
a.age = 50
# print(a.age)

class Employee ():
    # constructor method
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # // instance method
    def details(self):
        print("Employe", self.salary)
        print("Name", self.name)


first = Employee("Kush", 1000)
second  = Employee("raaa", 2000)

# first.details()

class ParentInfo:
    def __init__(self, name, number):
        print(f"my name is {name} & number is {number}")

    def myInstanc(self):
        print("print form instalce")

    # class method
    @classmethod
    def myName (cls):
        print("hellow classmethod")

    # static method
    def staticmethod():
        print("hellow world")

# x = ParentInfo('Ujjal', 9896867865)
# ParentInfo.myName()
# ParentInfo.myInstanc()
# y = x.myName()
# print(y)
# x.myInstanc()

# Inheritance

class Myfunction1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyFunction2(Myfunction1):
    pass

# p = MyFunction2("first name", 25)
# c = Myfunction1("zaman", 55)
# print(p.name)
# print(c.name)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area (self):
        return self.length * self.width

    def permeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        super().__init__(length, length)

    def area(self):
        return self.length * self.length
    
    def perimeter(self):
        return 4 * self.length
    
