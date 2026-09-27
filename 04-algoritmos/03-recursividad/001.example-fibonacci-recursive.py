def fibonacci_recursive(num):
    if (num == 1 or num == 0):
        return num
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)