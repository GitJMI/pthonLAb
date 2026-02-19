list = []
for i in range(20):
    list.append(i)

newL = []

for i in list:
    if i != 0:
        newL.append(i)
for i in list:
    if i == 0:
        newL.append(i)
        
print(newL)