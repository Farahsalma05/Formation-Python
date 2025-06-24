def addition(a,b):
    r=a+b
    return r

def subtraction(a,b):
    r=a-b
    return r
def multiplication(a,b):
    r=a*b
    return r
def division(a,b):
    r=a/b
    return r
def modulo(a,b):
    r=a%b
    return r
def power(a,b):
    r=1
    for i in range(int(b)):
        r=r*a
    return r
import math
print("Welcome to the Calculator!")
while True :
    print("Do you want to 'calcul' or 'exit'? ")
    choice_cal=input("").strip().lower()
    if choice_cal == "calcul" :
        print("Operations are :\n -addition \n -subtraction \n -multiplication \n -division \n -modulo \n -power \n -square root ")
        choice = input("Please choose an operation : ").lower().strip()
        try:
            if choice == "square root" :
                x = float(input("please enter your value : "))
                print(f"the square root of {x} is {math.sqrt(x)}")
            else :
                a = float(input("please enter your first value : "))
                b = float(input("please enter your second value : "))
                if choice == "addition" :
                    print(f"the addition of {a} and {b} is {addition(a,b)}")
                elif choice == "subtraction" :
                    print(f"the subtraction of {a} and {b} is {subtraction(a,b)}")
                elif choice == "multiplication" :
                    print(f"the multiplication of {a} and {b} is {multiplication(a,b)}")
                elif choice == "division" :
                    print(f"the division of {a} and {b} is {division(a,b)}")
                elif choice == "modulo" :
                    print(f"the modulo of {a} and {b} is {modulo(a,b)}")
                elif choice == "power" :
                    print(f"the power of {a} and {b} is {power(a,b)}")
                else :
                    print("invalid input")
        except ZeroDivisionError :
            print("you can't divide by zero , re-enter your values ")
        except ValueError :
            print("your value is false , re-enter your values ")
    elif choice_cal == "exit":
        print("Goodbye, see you soon !")
        break
    else :
        print("invalid input")