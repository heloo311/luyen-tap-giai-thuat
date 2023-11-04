from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""

        left = Counter(s)
        stack = []
        in_stack = set()

        for c in s:
            if c in in_stack:
                left[c] -= 1
                continue
            else:
                while stack and stack[-1] > c and left[stack[-1]] >= 1:
                    popped = stack.pop()
                    in_stack.remove(popped)

                stack.append(c)
                left[c] -= 1
                in_stack.add(c)

        ret = ''.join(stack)
        return ret

a= Solution()
s = "bcabc"
print(a.removeDuplicateLetters(s))