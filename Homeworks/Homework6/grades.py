filename="C:/Users/MSi/OneDrive/Bureau/Formation Python/Homeworks/Homework6/grades.csv"
mode="r"
lines=[]
with open(filename,mode) as f:
    lines=f.readlines()
    print(lines)

results=[]

for line in lines :
    student= line.strip().split(",")
    student_name=student[0]
    scores=0
    count=0
    for i in range (1,len(student)):
        score=int(student[i])
        scores+=score
        count+=1
    average = scores / count
    if average >= 50 :
        result = "Pass" 
    else :
        result="Fail"
    results.append(student_name + "," + str(round(average, 2)) + "," + result)

filename2 = "C:/Users/MSi/OneDrive/Bureau/Formation Python/Homeworks/Homework6/averages.csv"
mode2="w"
with open(filename2, mode2) as f:
    f.write('Student Name, Average, Result\n')
    for result in results:
        f.write(result + "\n")