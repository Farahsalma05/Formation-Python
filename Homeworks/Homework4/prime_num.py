def prime(num) :
    if num>1 :
        for i in range(2 , num) :
            if num%i == 0:
                print(f"{num} is not a prime number")
                return
        print(f"{num} is a prime number")
    elif num==1 :
        num=int(input("please enter another value greater than 1 : "))
        prime(num)
    else :
        num=int(input("invalid input , please enter another number : "))
        prime(num)
num=int(input("please enter a number : "))
prime(num) 