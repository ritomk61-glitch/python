class student:
    def __init__(self,name,sid,dept):
        self.name = name
        self.sid = sid
        self.dept = dept
    def shows(self):
        print(f"studnet name is {self.name}\nsystem id is {self.sid} \n department name is {self.dept}")

class hostelstudent(student):
    def __init__(self, name, sid, dept , roomno , hostelname , fees):
        super().__init__(name, sid, dept)
        self.roomno = roomno
        self.hostelname = hostelname
        self.fees = fees
    def showh(self):
        print(f"your hostel room no is {self.roomno} \n your hostel name is {self.hostelname} \n your fees is {self.fees}")
class allin(hostelstudent,student):
    def __init__(self, name, sid, dept, roomno, hostelname, fees):
        super().__init__(name, sid, dept, roomno, hostelname, fees)
h = allin("ritom" ,3434,"cse",222,"ramam hostel" , 2232323233)
h.shows()
h.showh()