#rock paper scissors game
x=input("rock, paper ,scissors :")
y=input("rock, paper ,scissors :")
if x==y :
    print("match null replay")
elif x=="rock" and y=="paper" :
        print("player 2 wins")
elif x=="rock" and y=="scissors":
        print("player 1 wins")
elif x=="paper" and y=="rock":
       print("player 1 wins")
elif x=="paper" and y=="scissors":
       print("player 2 wins")
elif x=="scissors" and y=="rock":
       print("player 2 wins")
elif x=="scissors" and y=="paper":
       print("player 1 wins")
else:
    print("invalid input")
    
    
    