# Write a program to check if a specific number is present in a list. Print "Found" if it exists and "Not Found" otherwise.

numbers = []

for index in range(5):
    while True:
        try:
            num = int(input(f"Enter number {index + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# for number in numbers:
while True:
    try:
        isNum = int(input("Enter a number you want to find : "))
        if isNum in numbers:
            print(f"Found")
            break
        else:
            print("Not found")
    except:
        print("Invalid input. Please enter a valid integer.")



# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial