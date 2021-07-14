speed =int(input("Enter a number: "))


def car(speed):
    count=0
    for i in range(1,speed+1,5):
            count=count+1
    #print(count)
    if count<=14:
        print("Ok")
    elif count>14 and count<27:
        print(count-14, "demerit points")
    else:
        print("Suspended")
car(speed)
