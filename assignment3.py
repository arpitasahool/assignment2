#1.create a list

a=['apple','mango' ,'banana']
print(a)

#2.concatenate two lists

a=['apple','mango' ,'banana']
b=[1,2,3]
print(a+b)

#3.count the occurance in a list

a=["apple","orange","banana","apple","apple","orange"]
for i in range(len(a)):
    b=a.count(a[i])
    print("%s : %s" %(a[i],b))

#4.sort the list

a=['o','i','e','a','u']
a.sort()
print(a)

#5.Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]

a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(n1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
n2=int(input("Enter number of elements:"))
for i in range(n2):
    d=int(input("Enter element:"))
    c.append(d)
c.sort()
new=a+c
print("Sorted list is:",new)

#6. Count even and odd numbers in that list

a=[]
c1=0
c2=0
b=int(input("enter num of elements"))
for i in range(b):
    c=int(input())
    a.append(c)
print(a)
for i in range(b):
    if a[i]%2==0:
        c1=c1+1
    elif a[i]%2!=0:
        c2=c2+1
print("count of even num are %s"%(c1))
print("count of odd num are %s"%(c2))

#8.max and min element in a tuple

a=(3,5,8,9,1,4,6)
print(max(a))
print(min(a))

#7.print tuple in a reverse order

a=(3,5,8,9,1,4,6)
print(a[::-1])

#9.print string in uppercase

a=input("enter string")
print(a.upper())

#10.check if the string contains the numeric character

a=input("enter string")
print(a.isnumeric())

#11.replace string with your name

a="my name is asmita"
b=a.replace('asmita','arpita')
print(b)



