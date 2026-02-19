list = [1,1,2,2,3,4,4,4,4,5,5,5,9,5,8,8,8,]
k = int(input("enter the value of K: "))

dict = {}

for i in range (len(list)):
    if dict.get(list[i]):
        dict[list[i]] += 1
    else:
        dict[list[i]] = 1

for keys in dict:
    if dict[keys] > k:
        print(f"{keys}")