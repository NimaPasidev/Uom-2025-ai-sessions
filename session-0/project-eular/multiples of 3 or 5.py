def sum_of_multiples(range_num): # range_num varible is needed to get value at a range
    total = 0   # varible to store sum
    for num3 in range(0,range_num,3): # getting values of multiples of 3 till the range_num
        total += num3 
    for num5 in range(0,range_num,5):# getting values of multiples of 5 till the range_num
        if num5%3 == 0: # if the value is already can divided by 3 pass
            pass
        else:
            total += num5
    return total

print(sum_of_multiples(1000))


# Time Complexity  = O(range_num)
# Space Complexity = O(1)