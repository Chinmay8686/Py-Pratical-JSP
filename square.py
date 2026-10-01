#accept two value S and N. print square of first N numbers starting from S 

s = int(input("Enter starting value S: "))
n = int(input("Enter number of values N: "))

for i in range(s, s + n):
    print(i, "->", i * i)