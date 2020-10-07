'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    for each in arr:
        if each == 0:
            arr.remove(each)
            arr.append(each)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")