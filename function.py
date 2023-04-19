num = int(input("enter the number"))

print(f"multiplication table for (num):")


def my_function(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")


my_function(num)
