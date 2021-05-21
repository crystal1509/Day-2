#WAP creates three lists from the user and finds the maximum of each list and performs addition, subtraction, multiplication on those elements.

list1=[70,80,60]
list2=[90,500,400]
list3=[1000,2000,500]
a=max(list1)
b=max(list2)
c=max(list3)

add=a+b+c;
sub=c-b-a;
mul=a*b*c;

print("addition:",add,"subtraction:",sub,"multiplication:",mul)
