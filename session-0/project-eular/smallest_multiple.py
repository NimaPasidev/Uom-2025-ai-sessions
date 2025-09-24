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


def prime_divider(number_list):  #this function get the number form list and divide it by its all prime factors
    prime_fac_list = []
    prime_list = []
    for x in number_list:
        prime_fac_num = []
        for num in range (x+1):
            if is_prime(num):
                while x% num == 0:
                    prime_fac_num.append(num)
                    if num not in prime_list:
                        prime_list.append(num)
                    x = x // num
        prime_fac_list.append(prime_fac_num)
    return (prime_fac_list,prime_list)

def overall_prime_max(prime_fac_list,prime_list): # this funtion count the max number of prime factors in the number list
    prime_count = []
    for prime in prime_list:
        highest_count = 0
        for lista in prime_fac_list:
            if lista.count(prime)>highest_count:
                highest_count = lista.count(prime)
        prime_count.append([prime,highest_count])
    return prime_count

def smallest_multipler(prime_count): # Calculate the least common multiple
    lcm = 1
    for count in prime_count:
        lcm *= count[0]**count[1]
    return lcm


number_range = 20
number_list = []
for number in range(1,number_range+1):
    number_list.append(number)

prime_fac_list,prime_list = prime_divider(number_list)
prime_count = overall_prime_max(prime_fac_list,prime_list)
print(smallest_multipler(prime_count))


# Time Complexity  = O(N*sqtr(N)*log(N))
# Space Complexity = O(N*log(N))