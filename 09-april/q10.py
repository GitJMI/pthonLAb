with open("file.txt") as f:
    bufferString = f.read()

bufferString = bufferString.lower()
words = bufferString.split( )
freq={}
for word in words:
    if word in freq:
        freq[word] +=1
    else:
        freq[word] =1
# print(freq)
search = input("Search Word:")
search = search.lower()
if search in freq:
    print(f"Occurrences of '{search}: {freq[search]}")
else:
    print("not found")
