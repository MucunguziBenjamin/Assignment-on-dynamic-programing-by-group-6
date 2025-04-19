#longest common subsequence
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    i, j = m, n
    lcs_str = []
    
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs_str.reverse()
    return dp[m][n], ''.join(lcs_str)

s1 = "ABCBDAB"
s2 = "BDCAB"

length, sequence = lcs(s1, s2)
print(length)
print(sequence)

 # Time Complexity: O(m * n) where m and n are the lengths of s1 and s2 respectively.
 # Space Complexity: O(m * n) for the dp array used to store the lengths of LCS.
