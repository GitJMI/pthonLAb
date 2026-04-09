with open("file.txt") as f:
    bufferString = f.read()

punc=['.',',','!','?']
newContent=""
for l in bufferString:
    if l not in punc:
        newContent += l

with open("clean.txt","w") as f:
    f.write(newContent)
