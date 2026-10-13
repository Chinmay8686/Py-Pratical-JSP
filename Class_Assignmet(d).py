
# Read a file, split its content into words, and store them in a list.
# i. Print the total number of words
# ii. Print all unique words

file_path = input("Enter the file path: ")

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()

# i. Print the total number of words
print("Total number of words:", len(words))

# ii. Print all unique words
unique_words = set(words)
print("Unique words:", unique_words)
