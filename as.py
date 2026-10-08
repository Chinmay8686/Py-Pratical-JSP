# Create a list of numbers and strings, accept values from the user,
# separate the list from the maximum number, and display the names in descending order.

# Create a list of numbers and strings, accept values from the user,
# separate the list from the maximum number, and display the names in descending order.

numbers = []
names = []

n = int(input("How many values do you want to enter? "))

for i in range(n):
    value = input("Enter value " + str(i + 1) + ": ")
    if value.isdigit():
        numbers.append(int(value))
    else:
        names.append(value)

if numbers:
    max_num = max(numbers)
    print("Maximum number is:", max_num)
else:
    print("No numbers were entered.")

print("Names in descending order:")
for name in sorted(names, reverse=True):
    print(name)
