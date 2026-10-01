#remove duplicate from list. ex: (23, 34, 23, 37, 48, 89) 1.list= 23, 34, 37, 48, 89)   
# Remove duplicate characters from a string

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)