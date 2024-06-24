# Read an integer input from the user
n = int(input()) # "Enter an integer: "

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

# Original list
numbers = [1, 2, 3, 4, 5]

# Squaring each element using a for loop
squared_numbers = []
for x in numbers:
    squared_numbers.append(x**2)

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
