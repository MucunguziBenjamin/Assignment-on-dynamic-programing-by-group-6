#matrix chain multiplication
def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):  # l is the chain length
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k

    return dp[0][n - 1], s

def print_optimal_parenthesization(s, i, j):
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage
p = [2, 3, 4, 5]  
min_cost, s = matrix_chain_order(p)
print(f"Minimum number of multiplications: {min_cost}")
print("Optimal Parenthesization: ", end="")
print_optimal_parenthesization(s, 0, len(p) - 2)
