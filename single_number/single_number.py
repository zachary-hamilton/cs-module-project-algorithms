'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    '''
    for i in range(len(arr)):
        to_check = arr[i]
        arr[i] = 'placeholdertext'
        if to_check not in arr:
            return to_check
        else:
            arr[i] = to_check
    '''
    v = set(arr)
    for num in arr:
        if num in v:
            v.remove(num)
        if num not in v:
            v.add(num)
    for n, i in v.items():
        if i == 1:
            return n


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")