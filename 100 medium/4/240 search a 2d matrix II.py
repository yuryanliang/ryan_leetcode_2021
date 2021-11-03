""" https://leetcode.com/problems/search-a-2d-matrix-ii/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])

        if not matrix:
            return False

        i = 0
        j = col -1 # upper right

        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1 # move left
            else:
                i +=1
        return False