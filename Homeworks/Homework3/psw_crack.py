characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","0","1","2","3","4","5","6","7","8","9","ç","é","à","&","~","#","'","(",")","[","]","-","|","`","_","^","@","°","+","=","¨","$","¤","£","ù","%","*","µ",",","?",";",".",":","/","!","§"," "]

psw = input("Enter your password : ")
count = 0
i = 0

while i < len(psw):
    for char in characters:
        count += 1
        if psw[i] == char:
            break
    i += 1

print(f"Your password is '{psw}' and to crack it it took {count} tries.")
