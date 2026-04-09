text = input("enter the string: ")
countV = 0
countC = 0
countD = 0
countS = 0
text = text.lower()

for l in text:
    if l in ['a','e','i','o','u']:
        countV += 1
    elif (l.isdigit()):
        countD += 1
    elif l == " ":
        countS += 1
    else:
        countC +=1

print(f"vowels:{countV}  digits:{countD} spaces:{countS} consonants:{countC}\n\n\n")


        

 