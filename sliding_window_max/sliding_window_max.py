'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    '''
    # this took about 34 sec to run
    start = 0
    end = k
    to_return = []
    while end <= len(nums):
        to_return.append(max(nums[start:end]))
        start += 1
        end += 1
    return to_return
    
    # this took about 34 seconds to run
    end = k
    to_return = []
    while end <= len(nums):
        to_return.append(max(nums[end - k:end]))
        end += 1
    return to_return
    
    # took about 41 sec to run
    return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]
    '''
    number_windows = len(nums) - k 
    current_max = max(nums[0:k])
    list_of_maxes = [current_max]
    for i in range(0, number_windows):
        if nums[k + i] > current_max:
            current_max = nums[k + i]
            list_of_maxes.append(current_max)
        else:
            if nums[i] >= current_max:
                current_max = max(nums[i+1:i+1+k])
            list_of_maxes.append(current_max)


        
            
    return list_of_maxes


    




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
