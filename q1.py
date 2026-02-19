list =[2,3,5,9,4]

# n = int (input("Enter the no. of elements: "))

# for i in range(0,n):
#     ele = int(input(f"enter the {i+1} element:"))
#     list.append(ele)


print(f"even elements in the {list} are")
for i in list:
    if i % 2 == 0:
        print(f"{i} ",end="")
print()        
print(f"elements at even positon are :")

for i in range(0,len(list),2):
    print(f"{list[i]} ",end="")