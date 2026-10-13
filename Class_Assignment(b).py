#read all lines from a file into a list. print the total number of lines and display te 2nd and 4 th line>


# Read all lines from a file into a list.
# Print the total number of lines and display the 2nd and 4th lines.

file_path = input("Enter the file path: ")

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))

if len(lines) >= 2:
    print("2nd line:", lines[1].strip())
else:
    print("2nd line does not exist.")

if len(lines) >= 4:
    print("4th line:", lines[3].strip())
else:
    print("4th line does not exist.")
