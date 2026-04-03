
class student:
    def __init__(self,name,roll,dept):
        self.name = name
        self.roll = roll
        self.dept = dept
    def show(self):
        print(f"hello student your name is {self.name}.your system id is {self.roll} and your dept is {self.dept}")

class teacher(student):
    def __init__(self,name,roll,dept,tname,tedu):

       super().__init__(name,roll,dept)
       self.tname = tname
       self.tedu = tedu 
    def showt(self):
        print(f"your teache name is {self.tname} and he is from {self.tedu}")
        print(f"hii there your name is {self.name}.your system id is {self.roll}.your department is {self.dept}your teache name is {self.tname} and he is from {self.tedu}")

d = teacher("ritom" , 3434 , "cse" , "harry" , "iit")
d.show()
d.showt()
