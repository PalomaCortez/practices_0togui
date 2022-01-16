## Cap 5 - Loops
#EX4 - Prime numbers

number_of_primes = 1000 #number of primes to display
n_of_primes_per_line = 10 #Display 10/line
count = 0 #count the number of prime numbers
number = 2 #a number to be tested for primeness

print("the first 50 prime numbers are: ")
while count < number_of_primes:
    #Assume the number is prime
    is_prime = True #is the current number prime?

    #Test if it is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If True, the number is not prime
            is_prime = False #set is_prime to False
            break #exit the for loop
        divisor += 1

    #Display the prime number and increase the count
    if is_prime:
        count += 1

        print(format(number, "5d"), end = '')
        if count % n_of_primes_per_line == 0:
            #display the number and advance for the new line
            print()

    #check if the next number is prime
    number += 1
