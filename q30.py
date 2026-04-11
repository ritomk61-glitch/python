class biodata(Exception):
    pass
class student():
    def __init__(self,name,roll,phy,che,mth):
        self.name = name
        self.roll = roll
        self.phy = phy
        self.che = che
        self.mth = mth
    def check(self):
        if(self.phy<0 or self.phy>100 or self.che<0 or self.che>100 or self.mth<0 or self.mth>100):
            raise biodata("please enter marks under 0 and 100")
        
    def display(self):
        print("name:",self.name)
        print("roll",self.roll)
        print("physic:",self.phy)
        print("chemistry:",self.che)
        print("math:",self.mth)

    def avg(self):
        return (self.phy+self.che+self.mth)/3
    
try:
      name = input("Enter Name: ")
      roll = int(input("Enter Roll Number: "))
      phy = int(input("Enter Physics Marks: "))
      che = int(input("Enter Chemistry Marks: "))
      mth = int(input("Enter Math Marks: "))

      s1=student(name,roll,phy,che,mth)
      s1.check()
      s1.display()
      print("percentage is :",s1.avg())

except biodata as e:
    print(e)




        
    