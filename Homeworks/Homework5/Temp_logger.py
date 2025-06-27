temps =[]
while True :
    temp=input("please enter a temperatures (or 'q' to finish): ").lower()
    if temp == "q" :
        break    
    temp =float(temp)
    temps.append(temp)
print("Temperatures : " ,temps)
print("Number of readings : " ,len(temps))
max_temp=temps[0]
min_temp=temps[0]
for i in range (len(temps)) :
    if max_temp < temps[i] :
        max_temp = temps[i]
    if min_temp > temps[i] :
        min_temp = temps[i]
avg =sum(temps) / len(temps)
print("the highest temperature is : ",max_temp)
print("the lowest temperature is : ",min_temp)
print("Average temperature: {:.1f}".format(avg))