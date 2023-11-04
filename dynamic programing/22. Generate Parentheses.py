from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp ={}
        dp[1] = ["()"]
        dp[2] = ["(())","()()"]
        for i in range(3,n+1):
            d= {}
            arr=[]
            for st in dp[i-1]:
                for j in range(0,len(st)):
                    new =st[0:j]+"()"+st[j:len(st)]
                    if new not in d:
                        d[new] =1
                        arr.append(new)
            dp[i] = arr
        return dp[n]

    # def generateParenthesis(self, n):
    #     if not n:
    #         return []
    #     left, right, ans = n, n, []
    #     self.dfs(left, right, ans, "")
    #     return ans
    #
    # def dfs(self, left, right, ans, string):
    #     if right < left:
    #         return
    #     if not left and not right:
    #         ans.append(string)
    #         return
    #     if left:
    #         self.dfs(left - 1, right, ans, string + "(")
    #     if right:
    #         self.dfs(left, right - 1, ans, string + ")")


a= 'abc'
print(a[0:3])

b={}
b[a] =1
print(b)
