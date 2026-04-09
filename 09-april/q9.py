with open("file.txt","r") as f:
    bufferString=f.read()

with open("target.txt","a") as file:
    file.write(f"\n{bufferString}")