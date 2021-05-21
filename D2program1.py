#Take user input, create a Python list, find a value in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

a=float(input("enter first no:"))
b=float(input("enter second no:"))
c=float(input("enter third no:"))
list1=[a,b,c]
print(list1)
d=float(input("enter a value to find and replace with 200:"))

find=list1.index(d)
list1[find]=200
print(list1)
