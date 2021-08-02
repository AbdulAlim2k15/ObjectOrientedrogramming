class car():
    def __init__(self,carmodel,carbrand):
        self.cmodel = carmodel
        self.cbrand= carbrand
    
class bus():
    def __init__(self,busmodel,busbrand):
        self.bmodel =busmodel
        self.bbrand = busbrand

class vehicle(car,bus):
    def __init__(self,owner,carmodel,carbrand,busmodel,busbrand):
        self.owner = owner
        car.__init__(self,carmodel,carbrand)
        bus.__init__(self,busmodel,busbrand)
    def display(self):
        print(self.owner)
        print(self.cmodel,self.cbrand)
        print(self.bmodel,self.bbrand)


trafic = vehicle("alim","ace2","ferary","xpro","BMW")
trafic.display()
