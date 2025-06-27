def prime(a) :
    if a>1 :
        for i in range(2 , a) :
            if a%i == 0:
                return 0
        return a
    elif a==1 :
        a=int(input("please enter another value greater than 1 : "))
        return prime(a)
    else :
        a=int(input("invalid input , please enter another number : "))
        return prime(a)
def PrimeN_inFactN(num):
    sum=0
    
    for i in range (2, num+1) :
        sum=sum+prime(i)
    print(f"The sum of prime numbers in the factorial of {num} is  {sum} ")
num=int(input("please enter a number :"))
PrimeN_inFactN(num)
