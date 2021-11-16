""" https://leetcode.com/problems/spiral-matrix/
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]
        return res

    def spiralOrder_1(self, matrix):
        res = []
        left = 0
        right = len(matrix[0]) -1
        top = 0
        bottom = len(matrix) -1

        while left <= right and top <= bottom:
            for i in range(left , right + 1):
                res.append(matrix[top][i])
            for j in range(top + 1, bottom):
                res.append(matrix[j][right])

            for i in reversed(range(left, right + 1)):
                if top < bottom:
                    res.append(matrix[bottom][i])
            for j in reversed(range(top + 1, bottom)):
                if left < right:
                    res.append(matrix[j][left])

            left +=1
            right -= 1
            top +=1
            bottom -=1
        return res


if __name__ == "__main__":
    print(Solution().spiralOrder([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]]))
