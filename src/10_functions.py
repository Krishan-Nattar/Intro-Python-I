# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def checkEven(number):
    if number % 2 == 0:
        return True

print(checkEven(4))
print(checkEven(3))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if num % 2 == 0:
    print("EVEN!")
else:
    print("ODD!")