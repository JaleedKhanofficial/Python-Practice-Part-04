# Write a program that takes a list of numbers and creates a new list containing only the odd numbers. Use a loop to achieve this.

print("** Filter Odd Numbers **")

# Initialize an empty list to store odd numbers
odd_numbers = []

# Loop to take input from the user
for _ in range(5):
    try:
        num = int(input("Enter a number: "))
        # Check if the number is odd
        if num % 2 == 1:
            odd_numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Print the list of odd numbers
print("Odd numbers entered:", odd_numbers)



# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial