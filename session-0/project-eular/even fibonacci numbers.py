def even_number_finder(number): # this function is for find even numbers 
    if number%2 ==0:
        return True
    else:
        return False
    
fibonacci_num_list = [1,2] # intialize first two numbers
last_val = 2 # set last value fo fibonacci list 
total_of_even_fibonacci = 2 # set a variable to get the sum of even fibonacci number
while last_val < 4000000: # iterate till four million
    last_val = fibonacci_num_list[-1]+fibonacci_num_list[-2] # update the last value fo list
    fibonacci_num_list.append(last_val) # append that value to list
    if even_number_finder(last_val): #check if it is even
        total_of_even_fibonacci += last_val

print(total_of_even_fibonacci)

# Time Complexity  = O(n)
# Space Complexity = O(n)

    