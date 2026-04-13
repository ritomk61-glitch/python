class student:
    su = "sharda university"
    def __init__(self , name , sysid , adress):
        self.name = name
        self.sysid = sysid
        self.adress = adress
    
class teacher(student):
    def __init__(self, name, sysid, adress,tname,spe,rate,gen):
        super().__init__(name, sysid, adress)
        self.tname = tname
        self.spe = spe
        self.rate = rate
        self.gen = gen
    def show(self):
        print(f"Hello!Your name is {self.name}.Your College Name is {self.su}.Your college system id {self.sysid}.Your Adress is {self.adress}")
    def showt(self):
        status = "Excellent teacher" if self.rate == 5 else "Good Teacher"
        gender = "He" if self.gen == "male" else  "She" #* Ternari operator
        print(f"Your faculty name is {self.tname}.{gender} is specielest in {self.spe} and {gender} have rated in their subject in {self.rate} {status}")

d = teacher("Ritom" , 2025834055 , "Bangladesh" , "Smita Tiwary" , "Python" , 4 , "male")
d.show()
d.showt()
        