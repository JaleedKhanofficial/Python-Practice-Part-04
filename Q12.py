# Write a program that takes a list of numbers and uses a loop to count how many even numbers are in the list.

print("** Count Even Numbers in a List **")

# Initialize an empty list to store odd numbers
even_numbers = []
sum = 0
# Loop to take input from the user
for _ in range(5):
            num = int(input("Enter a number: "))
            even_numbers.append(num)
            # Check if the number is Even, if the number is even the count or sum.
            if num % 2 == 0:
                sum = sum + num

# Print the list of numbers
print(f"List is : {even_numbers} ")

# Print the count of even number
print(f"Count of Even Number in List {sum}")



# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial