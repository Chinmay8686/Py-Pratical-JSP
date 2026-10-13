#Take a sentence from the user, split it inot words, abd store them in a list. print te longest word.


sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest_word = max(words, key=len)

# Display the longest word
print("Longest word:", longest_word)
