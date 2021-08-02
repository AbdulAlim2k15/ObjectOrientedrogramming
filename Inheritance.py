class student():
       
    # Constructor
    def __init__(self, name):
        self.name = name
   
    # To get name
    def getName(self):
        return self.name
   
    # To check if this person is an employee
    def isEngineer(self):
        return False
   
   
# Inherited or Subclass (Note Person in bracket)
class engineer(student):
   
    # Here we return true
    def isEngineer(self):
        return True
   
# Driver code
std1 = student("boss") 
print(std1.getName(), std1.isEngineer())
   
std2 = engineer("george") 
print(std2.getName(), std2.isEngineer())