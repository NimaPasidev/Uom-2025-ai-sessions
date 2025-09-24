def differene_calculate(number): #calculate the difference between sum squre and squre sum
    sum = 0
    sq_sum = 0
    for num in range (1,number+1):
        sum += num
        sq_sum += num**2

    sum_sq = sum **2
    return sum_sq - sq_sum

print(differene_calculate(100))

# Time Complexity  = O(N)
# Space Complexity = O(1)