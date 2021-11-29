""" https://leetcode.com/problems/unique-paths-ii/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.



Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1


Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        ob = obstacleGrid

        if not ob: return
        row = len(ob)
        col = len(ob[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]

        dp[0][0] = 1 - ob[0][0]

        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] * (1 - ob[i][0])
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] * (1 - ob[0][i])
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (1 - ob[i][j])
        return dp[-1][-1]


if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
