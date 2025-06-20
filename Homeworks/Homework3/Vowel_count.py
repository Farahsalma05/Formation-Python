#vowel counter
vowels=["a","i","e","o","u"]
word=input("enter a word :")
count=0
for char in word :
    if char in vowels :
        count=count+ 1
print("The number of vowels in this word is:", count)
