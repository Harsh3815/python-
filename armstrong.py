num = input("enter a number:")
n = len(num)
total = sum(int(digit) ** n for digit in num)
if total == int(num):
    print("armstrong")
else:
    print("not ")