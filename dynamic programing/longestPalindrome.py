class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # Create a table to store whether substrings are palindromes
        is_palindrome = [[False] * n for _ in range(n)]
        print(is_palindrome)

        start, max_length = 0, 1  # Initialize variables to track the longest palindrome found

        # All substrings of length 1 are palindromes
        for i in range(n):
            is_palindrome[i][i] = True

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                start = i
                max_length = 2

        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the current substring
                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length

        return s[start:start + max_length]

# Example usage:
solution = Solution()
print(solution.longestPalindrome("bcabacd"))