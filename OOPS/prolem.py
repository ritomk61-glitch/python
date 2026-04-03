class student:
    def __init__(self,name,roll,phy,math,chy,bio):
        self.name = name
        self.roll = roll
        self.phy = phy
        self.math = math
        self.chy = chy
        self.bio = bio
    
    def caltotal(self):
        print(f"your total mark is {self.math + self.chy + self.bio +self.phy}")
    def avg(self):
        print(f"your average is {(self.phy + self.math + self.chy + self.bio)/4}")




r=student("riom",34,55,88,55,76)
r.caltotal()
r.avg()
