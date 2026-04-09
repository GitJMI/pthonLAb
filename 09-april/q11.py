with open("file.txt") as f:
    bufferString = f.read()


with open("newFile.txt","w") as f:
    bufferString = bufferString.upper()
    f.write(bufferString)

