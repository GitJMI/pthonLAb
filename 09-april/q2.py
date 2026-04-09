text = input("enter the string: ")
newString =""
listW= text.split()

for word in listW:
    newString += word[::-1]
    newString +=" "
    
print(newString)