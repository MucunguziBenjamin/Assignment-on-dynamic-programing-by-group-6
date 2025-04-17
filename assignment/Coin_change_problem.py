#coin change problem
def coin_change(coins, amount):
    # Step 1: Initialize DP Table
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # Step 2: Fill DP Table
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Step 3: Return Result
    if dp[amount] == float('inf'):
        return -1, []  # No solution exists
    else:
        return dp[amount], find_combinations(coins, amount, dp)

def find_combinations(coins, amount, dp):
    combinations = []
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                combinations.append(coin)
                amount -= coin
                break
    return combinations

# Example usage
coins = [1, 2, 5]
amount = 11
min_coins, coin_combination = coin_change(coins, amount)
print(f"Minimum coins required: {min_coins}")
print(f"Coins used: {coin_combination}")
