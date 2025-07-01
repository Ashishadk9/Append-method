# Q1
N = int(input("How many number"))#input
#list to store the number
numbers=[]
# use for loop
for i in range(N):
    num=int(input("Enter a number"))
    numbers.append(num)
# Sum for evan and odd number
even_sum=0
odd_sum=0
# Number in the list
for num in numbers:
    if num % 2==0:
        even_sum +=num #add the even sum
    else:
      odd_sum +=num # add the odd sum
# Print
print("Sum of even number:",even_sum)
print("Sum of odd number:",odd_sum)