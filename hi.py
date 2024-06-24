x = int(input("n is :"))
print(f"{x}")
y = x % 2
print(f"{y}")
if y == 0:
    if x >=2 and x < 5:
        print("Not Weird")
    if x >=6 and x <=20:
        print("Weird")
    if x >20:
        print("Not Weird")
else:
    print("Weird")
#====
# Read an integer input from the user
n = int(input("Enter an integer: "))

# Conditional checks based on the given rules
if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
