def palindrome_genarator(max_num_of_digits):
    single_max_num = int(str(9)*max_num_of_digits)
    max_num_multiple = single_max_num**2
    max_num_multiple_digts = list(str(max_num_multiple))
    new_list_copy = max_num_multiple_digts[::]
    if len(max_num_multiple_digts)>1:
        if len(max_num_multiple_digts)%2 ==0:
            iterations = len(max_num_multiple_digts)//2
        else:
            iterations = len(max_num_multiple_digts)//2+1
        count = 0
        while iterations:
            if count == 0:
                if max_num_multiple_digts[0] != max_num_multiple_digts[-1]:
                    if max_num_multiple_digts[1] != 0:
                        new_list_copy[-1]= max_num_multiple_digts[0]
                        if int(max_num_multiple_digts [-1]) < int(max_num_multiple_digts[0]): 
                            max_num_multiple_digts[1]  = str(int(max_num_multiple_digts[1])-1)
                        max_num_multiple_digts.pop(0)
                        max_num_multiple_digts.pop(-1)
                        print(max_num_multiple_digts,new_list_copy)
                    else :
                        pass
            else :
                max_num_multiple_digts 
            iterations -= 1
            count += 1
    return new_list_copy

print(palindrome_genarator(3) )