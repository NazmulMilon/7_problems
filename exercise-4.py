limit = int(input("Enter a number:"))


def showNumbers(limit):
    for i in range(limit+1):
        if i%2==0:
            print(i,"Even")
        else:
            print(i,"Odd")
        i=i+1
    print("Finish")
showNumbers(limit)