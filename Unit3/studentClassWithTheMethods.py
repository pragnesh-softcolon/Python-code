# 9) Create a Student class with the methods set_id, get_id, set_name, get_name, set_marks and get_marks where the method name starting with the set are used to assign the values and method name starting with getting are returning the values.
# Save the program by student.py. Create another program to use the Student class which is already available in student.py.

class student:
    def setid(self,id):
        self.id=id
    def getid(self):
        return self.id
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setaddress(self,address):
        self.address=address
    def getaddress(self):
        return self.address
    def setmark(self,mark):
        self.mark=mark
    def getmark(self):
        return self.mark
    
s=student()
s.setid(10)
s.setname("raj")
s.setaddress("maninagar")
s.setmark(200)

print("ID",s.getid())
print("Name",s.getname())
print("Address",s.getaddress())
print("Marks",s.getmark())