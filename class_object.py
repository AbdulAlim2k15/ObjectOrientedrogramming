class Computer:
    def __init__(self,model,brand,ram,hdd,processror):
        self.model= model
        self.brand = brand
        self.ram = ram
        self.hdd = hdd
        self.processror = processror

    def display(self):
        print('Mobile specification \n')
        print(self.model,self.brand,self.ram,self.hdd,self.processror)
    

comp1 = Computer("lenovoideapad","lenovo","8gb","itb","intel_core-i7")
comp1.display()
      

