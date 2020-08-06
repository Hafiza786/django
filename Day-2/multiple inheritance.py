class classA:
    def A():
        return "iam from class A"
class classB:
    def B():
        return "iam from class B"
class classC(classA,classB):
    def C():
        return "iam from class C"
