class student:
    su = "sharda university"
    def __init__(self , name , sysid , adress):
        self.name = name
        self.sysid = sysid
        self.adress = adress
    
class teacher(student):
    def __init__(self, name, sysid, adress,tname,spe,rate):
        super().__init__(name, sysid, adress)
        self.tname = tname
        self.spe = spe
        self.rate = rate
        # self.gen = gen
    def show(self):
        print(f"Hello!Your name is {self.name}.Your College Name is {self.su}.Your college system id {self.sysid}.Your Adress is {self.adress}")
    def showt(self):
        print(f"Your faculty name is {self.tname}.She is specielest in {self.spe} and He/She have rated in their subject in {self.rate}")

d = teacher("Ritom" , 2025834055 , "Bangladesh" , "Smita Tiwary" , "Python" , 5)
d.show()
d.showt()
        