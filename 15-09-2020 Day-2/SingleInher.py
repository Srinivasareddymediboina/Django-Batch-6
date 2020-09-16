#Single Line Inheritance
class ClassA:
    a,b=11,14
    
    def display():
        return "I am from ClassA"
    def add():
        return ClassA.a+ClassA.b
    
class ClassB(ClassA):
    a,b,c=10,20,30
    def show():
        return "I am form ClassB"
    def sub():
        return ClassB.a-ClassB.c

    
    
    
