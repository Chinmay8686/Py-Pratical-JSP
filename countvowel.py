#accept sentence from user and count the vowels.
# Count vowels in a string

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)