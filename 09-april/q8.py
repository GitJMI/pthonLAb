with open("file.txt") as f:
    bufferString=f.read()

with open("target.txt","w") as file:
    file.write(bufferString)