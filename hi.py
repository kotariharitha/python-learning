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
