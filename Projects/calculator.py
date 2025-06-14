try:
    print("Operations are : addition , subtraction , multiplication , division , modulo")
    choice = input("choose the operation : ").lower().strip()
    a = float(input("please enter your first value : "))
    b = float(input("please enter your second value : "))
    if choice == "addition" :
        r=a+b
        print(f"the addition of {a} and {b} is : {r}")
    elif choice == "subtraction" :
        r=a-b
        print(f"the subtraction of {a} and {b} is : {r}")
    elif choice == "multiplication" :
        r=a*b
        print(f"the multiplication of {a} and {b} is : {r}")
    elif choice == "division" :
        r=a/b
        print(f"the division of {a} and {b} is :  {r}")
    elif choice == "modulo" :
        r=a%b
        print(f"the modulo of {a} and {b} is : {r}")
    else :
        print("invalid choice")
except ZeroDivisionError :
    print("you can't divide by zero , re-enter your values ")
except ValueError :
    print("your value is false , re-enter your values ")
