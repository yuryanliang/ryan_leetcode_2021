""" https://leetcode.com/problems/set-matrix-zeroes/
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

"""
先判断 0行 有么有0
0列 有没有0

做上true false 标记。

处理除了0行0列的值， 在0行0列上标记

回头处理 0行 0 列

我们考虑就用原数组的第一行第一列来记录各行各列是否有0.

- 先扫描第一行第一列，如果有0，则将各自的flag设置为true
- 然后扫描除去第一行第一列的整个数组，如果有0，则将对应的第一行和第一列的数字赋0
- 再次遍历除去第一行第一列的整个数组，如果对应的第一行和第一列的数字有一个为0，则将当前值赋0
- 最后根据第一行第一列的flag来更新第一行第一列
"""
# https://leetcode.com/problems/set-matrix-zeroes/discuss/657430/Python-Solution-w-approach-explanation-and-readable-with-space-progression-from%3A-O(m%2Bn)-and-O(1)

# Space: O(m + n)
class Solution:
    def setZeroes(self, matrix):
        if not matrix:
            return []

        row = len(matrix)
        col = len(matrix[0])

        zeroes_row = [False] * row
        zeroes_col = [False] * col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeroes_row[i] = True
                    zeroes_col[j] = True

        for i in range(row):
            for j in range(col):
                if zeroes_row[i] or zeroes_col[j]:
                    matrix[i][j] =0

    # Space: O(1)
    def setZero(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[row][0] ==0 or matrix[0][col] ==0 else matrix[row][col]

        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0