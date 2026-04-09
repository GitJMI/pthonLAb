text = input("enter the string:")
newText = ""
freq={}
# for l in text:
#     if l in freq:
#         freq[l] +=1
#     else:
#         freq[l] = 1

for l in text:
    if l in freq:
        freq[l] +=1
    else:
        freq[l] =1

    if freq[l] == 1:
        newText += l
        
print(f"{newText}")