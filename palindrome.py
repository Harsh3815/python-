num = input("enter a number to check number is palindrome :")
rev = num[::-1]
print("reversed number:",rev)
if num == rev:
    print("palindrome")
else:
    print("not a palindrome")