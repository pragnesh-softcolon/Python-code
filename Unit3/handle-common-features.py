# 5) Write a program to use class method to handle the common features of all the instances of the Student class.

class Student:
    semester=5
    @classmethod
    def study(cls,sem):
        print(" {} studies in semester {}".format(sem,cls.semester))
Student.study("sumit")