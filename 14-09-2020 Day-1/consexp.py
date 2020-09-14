class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        return {"Name":self.name,"RollNo":self.rollno}
    
        
