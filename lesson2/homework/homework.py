# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
x = int(input("Give me a number:"))
y = int(input("Give me a smaller number:"))
print("The quotient is", x // y)
print("The remainder is", x % y)
# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
animal = (input("What is your favourite animal?: "))
colour = (input("What is your favourite colour?: "))
print("A", colour, animal, "would be cool")
# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
print( )
for i in range (0, 11, 2):
    print(i)
# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
print( )
z = int(input("How many push-ups can you do in a day: "))
print("You can do", (z * 7), "push-ups in a week")
# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
for i in range (1, 7):
    print(i*i)