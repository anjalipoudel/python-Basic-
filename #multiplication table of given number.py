#multiplication table of given number
#get the number from user

num = int(input("enter a number:"))
#print the multiplication table
print(f"multiplication table for (num):")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
    print("%d x %d = %d")
