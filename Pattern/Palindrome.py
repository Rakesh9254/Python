text = input("Enter text : ").lower()
if text == text[::-1]:
    print("Palindrome string")
else:
    print("Not a Palindrome string")
