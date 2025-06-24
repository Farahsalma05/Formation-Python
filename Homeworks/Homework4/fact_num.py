def fact (num) :
    if num<=0 :
        num=int(input("enter a positive number : "))
        fact(num)
    else :
        r=num
        for i in range(1 ,num) :
            r=r*i
        print(f"the factorial of {num} is {r}")
num=int(input("please enter a number : "))
fact(num)