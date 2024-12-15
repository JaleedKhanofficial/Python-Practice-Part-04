# Write a program to take a list of numbers and use slicing to reverse it. Print the reversed list.

print("** Reverse a List **")

# Initialize an empty list to store numbers
numbers = []

# Loop to take 10 numbers as input from the user
for index in range(10):
    while True:
        try:
            num = int(input(f"Enter number at index {index}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Print the original list
print("Original list:", numbers)

# Reverse the list using slicing
reversed_numbers = numbers[::-1]

# Print the reversed list
print("Reversed list:", reversed_numbers)


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial