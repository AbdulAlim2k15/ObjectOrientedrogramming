class Employee:
    def __init__(self,name,designation,department,salary):
        self.EmplName = name
        self.designation = designation
        self.department = department
        self.salary= salary
        print("Employee Created  ")

    def __del__(self):
         print("employee deleted")
    
employee1 = Employee("abul","Assistant Manager1","ICT","80000ttk")
employee2 = Employee("babul","Subassistant Engineer","Electrical","35000tk")
del employee1