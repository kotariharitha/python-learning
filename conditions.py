x = int(input("x is :"))
y = int(input("y is :"))
# print(f"x: {x}, y: {y}, typeof(x): {type(x)}, typeof(y): {type(y)}")
if x<y: # 1
    print("x is less than y")
    print(f"{x} < {y}")
elif x>y: # 1 # else if in C 
    print("x is greater than y")
    print(f"{x} > {y}")
else: # 1
    print("x euqals to y")
    print(f"{x} = {y}")


# excution time
if x<y: # 1
    print("x is less than y")
    print(f"{x} < {y}")
if x>y: # 1
    print("x is greater than y")
    print(f"{x} > {y}")
if x==y: # 1
    print("x euqals to y")
    print(f"{x} = {y}")