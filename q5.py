list = [1,1,2,2,3,4,4,4,4,5,5,5,9,5,8,8,8,]

dict = {}


for i in range (len(list)):
    if dict.get(list[i]):
        dict[list[i]] += 1
    else:
        dict[list[i]] = 1



for keys in dict:
    print(f"{keys} : {dict[keys]}")
    
print("unique elements : ",end="")
for keys in dict:
    if dict[keys] ==1:
        print(f"{keys} " , end="")
print()
print("duplicate elemetns: ",end="")
for keys in dict:
    if dict[keys] != 1:
        print(f"{keys} " , end="")