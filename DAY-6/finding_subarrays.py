def find_zero_sum_subarrays(arr):
    sum_indices = {}
    cumulative_sum = 0
    result = []
    
    for i in range(len(arr)):
        cumulative_sum += arr[i]
        
        if cumulative_sum == 0:
            result.append((0, i))
        
        if cumulative_sum in sum_indices:
            start_indices = sum_indices[cumulative_sum]
            for start_index in start_indices:
                result.append((start_index + 1, i))
        
        if cumulative_sum in sum_indices:
            sum_indices [cumulative_sum].append(i)
        else:
            sum_indices[cumulative_sum] = [i]
    
    return result

print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1]))
print(find_zero_sum_subarrays([1, 2, 3, 4]))  
print(find_zero_sum_subarrays([0, 0, 0]))
print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))
print(find_zero_sum_subarrays([1, 2, -3, 3, -1, 2]*10000))