#password checker
psw="Python2025 "
psw=input("enter your password : ")
for i in range(9) :
    if psw == "Python2025 " :
        print("correct password")
        exit()
    else :
        print("invalid password")
        psw=input("enter a new one : ")
print("you have had 10 attempts , wait 10 seconds then try again ")