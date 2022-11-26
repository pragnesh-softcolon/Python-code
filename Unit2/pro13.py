def Salary(name,slr):
	da = (slr * 0.25)
	hra = (slr * 0.15)
	tax=float(input("enter the persentage of tax: "))
	ActualSalary = (slr+da+hra)-(tax/100)
	print("Name : ",name)
	print("Salary :",ActualSalary)

name=str(input("enter name of employee : "))
BasicSalary=int(input("enter the salary of the employee : "))
Salary(name,BasicSalary)