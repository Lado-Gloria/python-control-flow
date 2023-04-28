# Write a function that uses while, if and continue 
# statements to print all the even numbers between 0 and 50. 
def even_number():
    x =0
    while x<50:
        x+=1
        if x%2!=0:
         continue

        print(x)
# Write a function that takes an integer argument and prints 
# "Prime" if the number is prime, and "Not prime" if the number 
# is not prime.
  
def is_prime(n):
    n=7
    if n <= 1:
        print("Not prime")
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
    print("Prime")

    # write a function that takes a list of integers as
    #  input and prints the sum of all the even numbers in the list.
def list_of_int(num):
        sum =0
        for i in num:
            if i%2==0:
                sum+=1
        print(sum)
       

# Write a function that takes any two integers 
# as input, and prints the sum of all the numbers 
# between the two integers (inclusive) that are divisible by 3.
def two_integer(a,b):
    count =0
    for i in range(a,b+1):
        if i%3==0:
            count+=1
            print(count)


