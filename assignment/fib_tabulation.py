# fibonacci by tabulation (bottom up)
def fibonacci(n):
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for i in range(2, n + 1):
        next_fib = prev + curr
        prev = curr
        curr = next_fib
    
    return curr

# Example usage
if __name__ == "__main__":
    n = 10  
    print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")

# Time Complexity: O(n) - The function iterates through a loop n-1 times.
    # Space Complexity: O(1) - Only a constant amount of space is used for variables.
