from typing import List


class Solution:
    def generate_pascals_triangle_row(self,row):
        if not row:
            return [1]

        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)
        return next_row
    def getRow(self, rowIndex: int) -> List[List[int]]:

        triangle = []
        current_row = []

        for _ in range(rowIndex+1):
            current_row = self.generate_pascals_triangle_row(current_row)
            triangle.append(current_row)

        return triangle[-1]
a= Solution()
print(a.getRow(3))

print([1]+[1,1]+[1,2,1])