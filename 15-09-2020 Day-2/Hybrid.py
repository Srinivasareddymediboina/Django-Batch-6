#Hybrid Inheritance
class parent:
    def fun1():
        return "i am from fun1"
    
class Child(parent):
    def fun2():
        return "i am from fun2"
    
class Child1(parent):
    def fun3():
        return "i am from fun3"
    
class Child2(Child1,parent):
    def fun4():
        return "i am from fun4"

