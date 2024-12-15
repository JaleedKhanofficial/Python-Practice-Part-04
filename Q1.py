# Write a program that takes a list of numbers as input and uses a for loop to print each element.

print("** Print All Elements of a List **")

# Initialize an empty list to store numbers
numbers = []

# Loop to take input from the user
for count in range(5):
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Print the list of numbers
print("You entered:", numbers)



# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial