# Write a program that takes a list and two numbers (start and end) as input. Use slicing to extract and print the sublist between these indices.

print("** Extract a Sublist **")

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

# Print the complete list
print("Full list of numbers:", numbers)

# Input the start and end points for the sublist
while True:
    try:
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        if 0 <= start <= end <= len(numbers):
            break
        else:
            print("Invalid range. Please ensure 0 <= start <= end <= 10.")
    except ValueError:
        print("Invalid input. Please enter valid integers.")

# Extract and print the sublist
sublist = numbers[start:end]
print("Extracted sublist:", sublist)



# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial