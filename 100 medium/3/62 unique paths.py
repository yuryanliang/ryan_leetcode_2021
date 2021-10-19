""" https://leetcode.com/problems/unique-paths/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""

"""
二维dp 问题， 问一共有多少种走法

逐行扫描， 如果过界就是0种。 从up来有几种， 从left来有几种。
如果是第一个起始点就略过， 用开头的原始值

"""

class Solution:
    def uniquePaths(self, m, n):
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                up = dp[i - 1][j] if i -1 >= 0 else 0
                left = dp[i][j - 1] if j -1 >= 0 else 0
                if i == 0 and j == 0:
                    continue
                else:
                    dp[i][j] = up + left
        return dp[n -1][m -1] # return n - 1, m - 1, m是列， n是行

if __name__ == "__main__":
    print(Solution().uniquePaths(2, 3))