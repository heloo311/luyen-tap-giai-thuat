class Solution:
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p) + 1)] for i in range(len(s) + 1)]
        # dp = [[False]*(len(p)+1)]*(len(s)+1)
        print(dp)
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] != '*':
                break
            dp[0][j] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] in {s[i - 1], '?'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        print(dp)
        return dp[-1][-1]

a= Solution()
p="*a*b"
s="adceb"
print(a.isMatch(s,p))

dp = [[False for _ in range(len(p) + 1)] for i in range(len(s) + 1)]
dp1 = [[False]*(len(p)+1)]*(len(s)+1)
print(dp==dp1)