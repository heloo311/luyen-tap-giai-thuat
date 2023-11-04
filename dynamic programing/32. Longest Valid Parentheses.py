class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        final = []
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(s[i])
            if s[i] ==')':
                if len(stack) ==0:
                    pass
                elif stack[-1] == '(':
                    temp= stack.pop()
                    final.append(temp)
                    final.append(s[i])
            # if s[i] == ')' and len(stack) ==0:
            #     pass
            # if s[i] ==')' and stack[-1] == '(':
            #     temp= stack.pop()
            #     final.append(temp)
            #     final.append(s[i])
        return len(final)

a= Solution()
s = "()"
print(a.longestValidParentheses(s))

