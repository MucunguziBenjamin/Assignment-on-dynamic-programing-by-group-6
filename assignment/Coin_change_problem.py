#coin change problem
def coin_change(coins, amount):
   
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1, []  
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

# Time Complexity: O(n * m), where n is the amount and m is the number of coin denominations
# Space Complexity: O(n), where n is the amount (for the dp array)
