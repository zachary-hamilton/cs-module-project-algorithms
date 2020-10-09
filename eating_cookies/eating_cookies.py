'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, mycache):
    '''
    # this is terribly slow
    # no or negative cookies
    if n <= 0:
        return 1
    # 1 cookie
    if n == 1:
        return 1
    # 2 cookie
    elif n == 2:
        return 2
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    '''
    #this is fast but will try again using recursion and cache
    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    num1 = 1
    num2 = 1
    num3 = 2
    for _ in mycache:
        number_ways = num1 + num2 + num3
        num1 = num2
        num2 = num3
        num3 = number_ways
    return number_ways
    
    '''
    if n <= 0:
        return 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies(n - 1, mycache) + eating_cookies(n - 2, mycache) + eating_cookies(n - 3, mycache)
    '''
    


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
