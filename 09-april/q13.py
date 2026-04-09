with open("file.txt") as f:
    bufferString = f.read()

words = bufferString.split()
size={}
for word in words:
    size[word] = len(word)


len = 0
for word in size:
    if len