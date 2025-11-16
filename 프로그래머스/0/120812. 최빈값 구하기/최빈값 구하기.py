def solution(array):
    index_arr = [0] * 1001
    count = 0
    num_set = set(array)
    
    for num in num_set:
        index_arr[num] = array.count(num)
    
    mode_num = max(index_arr)
    
    for num in num_set:
        if index_arr[num] == mode_num:
            count += 1
        
        if count > 1:
            return -1
    
    return index_arr.index(mode_num)