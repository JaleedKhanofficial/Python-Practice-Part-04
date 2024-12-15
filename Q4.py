# Write a program that takes two lists of numbers as input and concatenates them into a single list. Print the combined list.

print("** Combine Two List **")
print("** Concatenate Two Lists **")

# Function to input numbers into a list
def input_list(prompt):
    print(prompt)
    while True:
        try:
            # Ask the user for a list of numbers
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            return numbers
        except ValueError:
            print("Invalid input. Please enter only integers separated by spaces.")

# Take input for the first and second lists
list1 = input_list("Enter the first list of numbers:")
list2 = input_list("Enter the second list of numbers:")

# Concatenate the two lists
combined_list = list1 + list2

# Print the combined list
print("Combined List:", combined_list)



# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial