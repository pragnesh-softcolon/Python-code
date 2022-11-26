# Write a program to find out and display the common and the non-common elements in the list using membership operators. ( Gujarat University BCA Sem5 Python Practical )
a = [1,2,3,4]
b = [5,6,7,8,4]
res=[]

for i in a:
    if i not in b:
        res.append(i)
for i in b:
    if i not in a :
        res.append(i)

print ("The uncommon of two lists is : ", res)
print("The common of two lists is : ",i)