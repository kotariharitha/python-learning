#name = input("what is your name")
#a=1
#print("a")
#print("hello")
#a=1
#b=2
#c=a+b
#print(f"{c}")
#name = input("what is your name")
#print("hello")
#print(name)
# adding name in one print
#print("hello"+ name) 
# here + is used for string concatnation so hello and name will display in one line
#print("hello",name) # withou + it will give alot space betweem hello and name 
#name = name.strip() # Remove white space from string
#name = name.capitalize() # cptalize user name
#name = name.title() # captilize total name even we have space between tow names like (haritha kotari)
#name = name.strip().capitalize()
#name = name.strip().title()
#print(f"hello,{name}")
# name = input("what is your name").strip().title()
# first= name.split(" ")  #split will split the name
# print(f"hello, {first}")
#print(f"hello,{name}")

name = input("Enter your full name: ")
"""
Split examples:
name = "Haritha Kotari"
name.split()
['Haritha', 'Kotari'] # this is a list contains 2 indexes
# Haritha is in index 0, Kotari is in index 1
first = name.split()[0] # here 0 in your list first index
"""
first= name.split(" ")[0]  # split will split the name to a list 
print(f"Hello, {first}")

first, last = name.split()
print(f'Hello, {first}')

a = f'Hello, {first} {last}'
print(a)

b = 'Hello, {} {}'.format(first, last)
print(b)

c = 'Hello, {a} {b}'.format(a=first, b=last)
print(c)