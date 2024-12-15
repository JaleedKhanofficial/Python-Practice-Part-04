# Write a program to create an empty list and add numbers to it one by one using a loop. Stop taking inputs when the user enters -1, and then print the final list.

print("** Dynamic List Input **")

# Initialize an empty list to store numbers
numbers = []

print("Enter numbers to add to the list. Type -1 to stop.")

while True:
    try:
        # Take user input
        num = int(input("Enter a number (-1 to stop): "))
        
        # Break the loop if user enters -1
        if num == -1:
            break
        
        # Add the number to the list
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Print the final list
print(f"Final List: {numbers}")


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial