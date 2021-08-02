class student():
    def __init__(self,name,dept):
        self.name = name
        self.department = dept
    
    def display():
        print(self.name,self.department)

class teacher(student):
    def __init__(self,name,dept,post,salary):
        self.post = post
        self.salary = salary

        student.__init__(self,name,dept)
    
    def show(self):
        print(self.name,self.department,self.post,self.salary)

std1 = teacher("alim","cse","assistant Professor",50000)
std1.show()
        