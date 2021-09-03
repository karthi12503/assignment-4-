#pattern 1
num=int(input("Enter the number of rows :"))
for row in range(num+1):
    for coloumn in range(row):
        print(row, end = ' ')
    print(" ")
#pattern 2
num=int(input("Enter the number of rows :"))
for row in range(1,num+1):
    for coloumn in range(num+1,row,-1):
        print(row, end = ' ')
    print(" ")
#pattern 3
num=int(input("Enter the number no.of rows :"))
value1=1
value2=0
include1=2
rem=0
for i in range(1,num+1):
    for j in range (1,i+1):
         rem=j
         if(rem==1):
            print(value1,end=" ")
         elif(rem>1):
            value2=value1-rem+1
            print(value2,end=" ")
         else :
            print("Wrong input", end= " ")
    value1=value1+include1
    include1=include1+1
    print( )
#pattern 4
num=int(input ("Enter the number of rows:"))
i=0
for row in range(0,num):
   for coloumn in range(0,num-row-1):
       print(" ",end=" ")
   for coloumn in range(0,row*2+1):
       i=row+1;
       print(i,end=" ")
   print()      
