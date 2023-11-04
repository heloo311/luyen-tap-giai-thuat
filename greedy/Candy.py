from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = n*[1]
        for i in range(1,n):
            if ratings[i] > ratings[i -1]:
                candies[i] = candies[i-1] +1
        for i in range(n-2 , -1 ,-1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)



a= Solution()
ratings = [1,0,2]
print(a.candy(ratings))


