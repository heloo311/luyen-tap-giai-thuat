from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        print(backward)

a= Solution()
words = ["abcd","dcba","lls","s","sssll"]
print(a.palindromePairs(words))

word = 'abvghj'
print(word[2:])
print(word[2-1::-1])
print(word[:2-1:-1])