class Student:
    def __init__(self,name,dept):
        self.name = name
        self.department = dept
    
    def show(self):
        print("I am "+self.name+ " and I am a graduate of "+self.department)
    
std1 = Student("alim","Computer Science and Engineering")
std2 = Student("Ahana", "Indermdiate second")
std1.show()
std2.show()