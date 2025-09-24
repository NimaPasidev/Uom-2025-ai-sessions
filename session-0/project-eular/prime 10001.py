import math

def is_prime(number):
    """
    Checks if a given number is a prime number.

    Args:
        number: An integer to be checked for primality.

    Returns:
        True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if number == 2:
        return True  # 2 is the only even prime number
    if number % 2 == 0:
        return False  # Other even numbers are not prime

    # Check for divisibility from 3 up to the square root of the number,
    # considering only odd numbers
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime

num = 1
prime_count =0 
given_prime = 10001
while prime_count != given_prime:
    if is_prime(num):
        prime_count += 1
        if prime_count == given_prime:
            print (num)
            break
    num += 1

# Time Complexity  = O(N*sqtr(N))
# Space Complexity = O(1)