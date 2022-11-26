li=[1,2,3,3,4,1,5,5,5,6,6,7,7,12,13]
li2=[]
for i in li:
    if i not in li2:
        li2.append(i)
print(li2)