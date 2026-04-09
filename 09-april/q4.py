text= input("enter the string:")
freq = {}

for l in text:
    if l in freq:
        freq[l] +=1
    else:
        freq[l] = 1

for l in freq:
    print(f"{l}: {freq[l]}")
    