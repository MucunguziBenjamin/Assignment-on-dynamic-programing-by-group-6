# Fibonacci function using memoization (top-down approach)
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    
    if n<=1:
        return n
    else:
        memo[n]=fib(n-1)+fib(n-2)
        return memo[n]
n=5
print(f"The {n}-th Fibonacci number is:{fib(n,memo={})}")

# Time Complexity: O(n) - Each Fibonacci number is computed once.
# Space Complexity: O(n) - The memo dictionary stores n Fibonacci numbers.
