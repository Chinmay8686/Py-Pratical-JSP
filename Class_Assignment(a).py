#write a program to read a file and count ow many vowels are present in its content . Is this code correct ?

def count_vowels_in_file(file_path):
    vowels = "aeiouAEIOU"
    count = 0

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    for char in text:
        if char in vowels:
            count += 1

    return count


if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    total_vowels = count_vowels_in_file(file_path)
    print(f"Total vowels in the file: {total_vowels}")
