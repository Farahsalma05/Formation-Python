#the average of a module 
x=float(input("enter your exam mark :"))
y=float(input("enter your tutorial mark 'TD' :"))
z=float(input("enter your lab work mark 'TP':"))
if x<0 or y<0 or z<0:
    print("invalid input")
    exit()
if x in range(0,20):
    if y in range(0,20) and z==0:
         avg=(x*0.6)+(y*0.4)
         print("your average of the module is :",avg)
    elif y==0 and z in range(0,20):
        avg=(x*0.6)+(z*0.4)
        print("your average of the module is :",avg)
    elif y in range(0,20) and z in range(0,20):
        avg=(x*0.4)+(y*0.2)+(z*0.2)
        print("your average of the module is :",avg)
