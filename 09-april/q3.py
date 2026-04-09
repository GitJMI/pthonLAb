text = input("enter the text:")

new = text.lower()

if new[::-1] == new:
    print(f"palindrome")
else:
    print("not a palindrome")