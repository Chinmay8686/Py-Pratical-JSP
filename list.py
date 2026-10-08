#create a list of 10 numbers, print the sum of last four elements of the list. find te difference 
# between maximum and minimum element of the list. insert a number in a list at 6th position this 
# number must be 1/3rd of number stored at fourth position. 
# 1st funciton length len(numbers), sum sum(numbers), sorted(numbers) Ascending order and descending, reverse = 2  

#create a list of 10 elements (string), print the sum of last 4 elemets of the list. find the difference between max and min elements of the list. 
#inser a number at 6th position of the list. this number must be 1/3 of number stored at 4th position of the list. print the updated list.
#different functions on the list - length, sum, sorted, reverse. without using f placeholder, print the length, sum, sorted and reverse of the list.

list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


#sum of last 4 elements
sum_last_4 = sum(list1[-4:])
print("Sum of last 4 elements:", sum_last_4)

# diff between max and min elements
diff = max(list1) - min(list1)
print("Difference between max and min elements:", diff)

#insert a number at 6th position
#this number must be 1/3 of the number stored at 4th position
list1.insert(5, list1[3] / 3)
print("Updated list:", list1)

#different functions on the list
print("Length of the list:", len(list1))
print("Sum of the list:", sum(list1))
print("Sorted list:", sorted(list1))
print("Reversed list:", list1[::-1])