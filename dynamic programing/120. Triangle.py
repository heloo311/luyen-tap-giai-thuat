from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        # Create a copy of the triangle to store the minimum sums
        dp = [[0] * len(row) for row in triangle]

        # Initialize the top row of dp with values from the triangle
        dp[0] = triangle[0]

        # Start from the second row and work your way down
        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])

        return min(dp[-1])

triagal=[[-1],[2,3],[1,-1,-3]]
a=Solution()
print(a.minimumTotal(triagal))


