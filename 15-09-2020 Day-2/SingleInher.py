#Single Line Inheritance
class ClassA:
    global a,b
    a,b=10,25
    def display():
        return "I am from ClassA"
    def add():
        return a+b
    
class ClassB(ClassA):
    a,b,c=10,20,30
    def show():
        return "I am form ClassB"
    def sub():
        return ClassB.a-ClassB.c
    
    
    
