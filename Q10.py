# Write a program that takes a list of numbers as input and uses max() and min() to find and print the largest and smallest numbers.

print("** Find Maximum and Minimum **")

# Initialize an empty list to store numbers
numbers = []

# Loop to take 11 numbers as input from the user
for index in range(11):
    while True:
        try:
            num = int(input(f"Enter number {index + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Print the original list
print(f"Original list: {numbers}")

# Find the maximum and minimum numbers
max_number = max(numbers)
min_number = min(numbers)

# Print the results
print(f"Maximum number is: {max_number}")
print(f"Minimum number is: {min_number}")



# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial