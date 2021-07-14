limit = int(input("Enter a number: "))


def add(limit):
    sum=0
    for i in range(1,limit+1):
        if i%3==0 or i%5==0:
            sum=sum+i
            print(i)
            i=i+1
    print("The summation of all numbrs is:", sum)

add(limit)