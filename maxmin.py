def max_min(lst):
    max_num = lst[0]
    min_num = lst[0]

    for num in lst:
        if num >= max_num:
            max_num = num 
        elif num <= min_num:
            min_num = num
               
    return [min_num, max_num]         


int_lst = [100, -100]
print(max_min(int_lst))

