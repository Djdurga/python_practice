def fib(num):
    if num == 0:
        return 0  # Base case: F(0) = 0
    elif num == 1:
        return 1  # Base case: F(1) = 1
    else:
        return fib(num-1) + fib(num-2)  # Recursive formula: F(n) = F(n-1) + F(n-2)

print(fib(9))  # Should print 34
