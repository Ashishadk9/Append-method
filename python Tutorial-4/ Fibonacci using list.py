# Number of  Fibonacci number to generate
n =10
#Start with first two number
fib =[1,1]
# Generate
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2]) # Add sum of last two
    print(fib)