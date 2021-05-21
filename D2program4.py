#WAP to take  user input of 4 students. Get the student Name, marks n 3 subjects and calculate their percentage. Also display each student's details.

n1=input("enter name:")
a1=float(input("enter first sub marks:"))
b1=float(input("enter second sub marks:"))
c1=float(input("enter third sub marks:"))
avg1=(a1+b1+c1)/3;
print("percentage:",avg1,"%")
list1=[n1,a1,b1,c1,avg1]


n2=input("enter name:")
a2=float(input("enter first sub marks:"))
b2=float(input("enter second sub marks:"))
c2=float(input("enter third sub marks:"))
avg2=(a2+b2+c2)/3;
print("percentage:",avg2,"%")
list2=[n2,a2,b2,c2,avg2]


n3=input("enter name:")
a3=float(input("enter first sub marks:"))
b3=float(input("enter second sub marks:"))
c3=float(input("enter third sub marks:"))
avg3=(a3+b3+c3)/3;
print("percentage:",avg3,"%")
list3=[n3,a3,b3,c3,avg3]

list1.extend(list2)
list1.extend(list3)
print(list1)
