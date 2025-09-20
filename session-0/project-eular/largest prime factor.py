import math

def largest_prime_factor(number):
    largest_prime = 1 
    while number%2 == 0: #biggest even prime is 2
        largest_prime = 2
        number //= 2
    i = 3 #handling odds
    while i * i <= number: #get a odd number and divide the given number until it divides completely
        while number % i == 0:
            largest_prime = i
            number //= i
        # Increment by 2 to skip even numbers.
        i += 2

    # If the remaining number is a prime factor greater than 2.
    if number > 2:
        largest_prime = number
    return largest_prime

print(largest_prime_factor(600851475143))

# Time Complexity  = O(sqrt(number))
# Space Complexity = O(1)
