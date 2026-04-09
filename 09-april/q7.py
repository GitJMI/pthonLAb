with open("file.txt") as f:
    bufferString=f.read()

lines = bufferString.split("\n")
words = bufferString.split( )

print(f"lines: {len(lines)}\nwords: {len(words)}\ncharacters: {len(bufferString)}")