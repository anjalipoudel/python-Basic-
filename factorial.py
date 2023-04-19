num = int(input("enter the number"))
print(f"factorial table for {num}:")


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")
