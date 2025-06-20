#Rock–Paper–Scissors with Replay (Best to three)
i=0
scr1=0
scr2=0
while i<3 :
    x=input("rock, paper ,scissors :")
    y=input("rock, paper ,scissors :")
    if x==y :
        print("match null replay")
        continue
    elif (x=="rock" and y=="scissors") or (x=="paper" and y=="rock") or (x=="scissors" and y=="paper") :
        print("player 1 wins this round")
        scr1=scr1+1
    elif (x=="rock" and y=="paper") or (x=="paper" and y=="scissors") or (x=="scissors" and y=="rock"):
       print("player 2 wins this round")
       scr2=scr2+1
    else:
        print("invalid input")
        continue
    i+=1
if scr1 > scr2 :
    print("player 1 wins the game with score :",scr1)
else :
    print("player 2 wins the game with score :",scr2)  