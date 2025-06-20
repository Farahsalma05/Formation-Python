vowels=["a","i","e","o","u"]
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
letter=input("enter a letter : ")
if letter in vowels :
    print("your letter is a vowel")
elif letter in consonants :
    print("your letter is a consonant")
else :
    print("invalid character")