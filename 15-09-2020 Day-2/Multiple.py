#Multiple Inheritance
class A:
    def ClassA():
        return "I am from ClassA"

class B:
    def ClassB():
        return "I am from ClassB"

class C(A,B):
    def ClassC():
        return " I am from ClassC"
