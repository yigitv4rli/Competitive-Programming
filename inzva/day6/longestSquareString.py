def longestCommonSubsequence(text1, text2):
    dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

    text1 = " " + text1
    text2 = " " + text2

    for i in range(1, len(text1)):
        for j in range(1, len(text2)):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


n = int(input())
s = input()
result = 0
for i in range(1,len(s)):
    result = max(result, longestCommonSubsequence(s[:i],s[i:]) * 2)
    
print(result)
