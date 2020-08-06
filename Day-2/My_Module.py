''' Modules And Packages :
   1.Modules : - It is a .py file.It contains classes and functions.
                       - By using import keyword module can be accesed.
                       eg: import time
                            time.ctime()- current time
                        eg: import os
                              os.getcwd() -current working directory
                        eg. import keyword
                               keyword.kwlist
     for accessing modules we have few different ways
               import My_Module
   2.Packages : - (folder)
                        - It is a collection of modules
                        -from package import modules(from APSSDC1 import My_Module)
                        - To grt all modules from package
                        -from package import*( from APSSDC1 import *)
                        - from pacakage import module (multilevel)(from APSSDC1.multilevel import classB)

 example:
import My_Module
>>> number()
1
2
3
4
5
6
7
8
9
>>> import My_Module.EvenorOdd(25)
SyntaxError: invalid syntax
>>> import My_Module
>>> My_Module.EvenorOdd(25)
'IS Odd'
>>> My_Module.cse()
'wlcome to CSE department'
>>> My_Module.classA.A()
'i am from class A'
                              
'''


def number():
    for i in range(1,10):
        print(i)
def EvenorOdd(a):
    if a%2==0:
        return "Is Even"
    return "IS Odd"

class classA:
    def A():
        return "i am from class A"

def cse():
    return "welcome to CSE department"
