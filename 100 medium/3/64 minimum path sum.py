"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

"""
二维dp问题。 dp[i][j]= grid[i][j] + min(dp[i-1][j], dp[i][j - 1])
如果过界， 把值设为maxsize
跳过初始点
"""
class Solution:
    def minPathSum(self, grid):
        n = len(grid) # row
        m = len(grid[0]) # col

        #populate the first row using m
        for i in range(1, m):
            grid[0][i] = grid[0][i] + grid[0][i-1]

        # populate the first col using n
        for j in range(1, n):
            grid[j][0] = grid[j][0] + grid[j-1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[j][i] = min(grid[j -1][i], grid[j][i-1]) + grid[j][i]
        return grid[-1][-1]
