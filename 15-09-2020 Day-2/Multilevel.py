#Multilevel Inheritance
class A:
    def ClassA():
        return "I am from ClassA"
class B(A):
    def ClassB():
        return "I am form ClassB"
class C(B):
    def ClassC():
        return "I am from ClassC"
