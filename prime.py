num = int(input("enter a number:"))
if num<2:
    print("not a prime number")
else:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print("not a prime number")
            break
        else:
            print("prime number")