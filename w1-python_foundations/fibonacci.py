def nth_fibonacci_number(n):
    """
    Return the n-th Fibonacci number.
    Raises ValueError if n is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError(f"n must be a positive integer.")
    
    if n == 0:   return 0
    elif n <= 2: return 1
    else:
        prev_num, curr_num = 1, 1
        for i in range(3, n+1):
            prev_num, curr_num = curr_num, prev_num+curr_num
        return curr_num

if __name__ == "__main__":
    print(nth_fibonacci_number(7))