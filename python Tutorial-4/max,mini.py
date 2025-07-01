# Q2
# Input of element
N =int(input("Enter how many number we need"))
# Store the numbers
numbers =[]
# Input N numbers and add
for i in range(N):
    num = int(input("Enter a numbers:"))
    numbers.append(num)
# Element is max and min
max_num= numbers[0] 
min_num = numbers[0] 
# Using loop
for num in numbers:
    if num>max_num:
        max_num= num
    if num < min_num:
        min_num = num
print("List of numbers:",numbers) # print the whole list
# Print the maximum & minimum number
print("Maximum number:", max_num)
print("Minimum number:", min_num)
