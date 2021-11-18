""" https://leetcode.com/problems/search-a-2d-matrix/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution:
    def searchMatrix(self, matrix, target):
        # if not matrix or not matrix[0]:
        #     return False
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row * col -1

        while left < right:
            mid = (left + right) //2
            mid_val = matrix[mid // col][mid % col]
            if mid_val < target:
                left = mid + 1
            else:
                right = mid
        return matrix[left // col][left % col] ==target


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    # matrix =[[1, 1]]
    print(Solution().searchMatrix(matrix, 3))