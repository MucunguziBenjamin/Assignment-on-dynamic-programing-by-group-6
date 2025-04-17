#fibonnaci by memoisation (top down)
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
