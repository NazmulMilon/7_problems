'''
#using for loop
num = int(input("Enter a number:"))
count = 0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("The number is a prime number.")
else:
    print("The Number is not a prime number. ")
'''

#using while loop
num = int(input("Enter a  number:"))
i=1
c=0
while i<=num:
    if num%i==0:
        c=c+1
    i=i+1
if c==2:
    print("Number is Prime.")
else:
    print("Number is not prime.")
