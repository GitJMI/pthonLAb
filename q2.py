list = []

for i in range(1,21):
    list.append(i)
    #list =[1,2,3,...20]

listN=[]
for i in range(3,18,2):
    listN.append(i)

print(f"2nd list = {listN}")
print("the sum of list is: ",end="")
sum = 0
for i in listN:
    sum +=i
print(sum)