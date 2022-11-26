# Write a python program that removes any repeated items from the list so that each item appear at most once.

lst=[1,1,2,3,4,3,0,0]
print("old list with repeated elements:",lst)
lst1=set(lst)
lst2=set(lst1)
print("new list with unique elements:",lst2)
