class classA:
    a=20
    b=30
    def display():
        return "i am from class A"

class classB(classA):
    c=20
    d=87
    def show():
        return "i am from classB"

    def add():
        return classB.c+classB.d
