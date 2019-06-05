a = "Hello World"

# Indexing
print(a[0])
print(a[-1])

#Slicing
print(a[0:5])

#STEP IN SLICING

print(a[0:10:2])  # Here 2 is refering to the number of steps to skipped between alphabets.

#Reverse of a string

print(a[:-1])
print(a[::-1])

# METHODS
x = input("Enter first name : ")
y = input("Enter last name : ")
print("Hello" + " " + x + " " + y)
print("Hello" + " " +x.upper() + " " + y.upper())
print("Hello" + " " + x.capitalize() + " " + y.capitalize())