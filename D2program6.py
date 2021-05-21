#WAP to get an employee ID, number of total days present,
#and wages per day using list. Calculate the basic pay,
#house rent allowance 10%, Dearness Allowance 5%,
#provident fund 12% to find the net salary.

ids=int(input("enter employee id:"))
p=int(input("enter total days present:"))
w=int(input("wages per day:"))
b=int(input("basic pay:"))
list1=[ids,p,w,b]
print(list1)

h=b*0.1;
d=0.05*b;
pf=0.12*b;
net=h+d+pf+b;

print(net)
 

 
