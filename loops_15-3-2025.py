# Task:- 
# 1.take input number from user and print the factors of that number
# num = int(input("enter a number"))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i, end=' ')



#  2.print the tables from 1-5 with multiplying of even numbers
num = int(input("please enter a number: "))
for i in range(1,num+1):
    print("table of ",i)
    for j in range(1,11):
        if j%2==0:
            print(i, "X ", j ," = ", i*j)
