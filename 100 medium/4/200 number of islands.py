""" https://leetcode.com/problems/number-of-islands/
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Sol:
    def numIslands(self, grid):
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, row, col, i, j) # start to explore
                    count +=1
        return count
    def dfs(self, grid, row, col, i, j):
        if grid[i][j] == '0':
            return
        grid[i][j] = '0' # change cell to visited, (flooded)
        if i > 0:
            self.dfs(grid, row, col, i -1, j)
        if i < row - 1:
            self.dfs(grid, row, col, i+ 1, j) #row -1 means can move one more
        if j >0:
            self.dfs(grid, row, col, i, j -1)
        if j< col -1:
            self.dfs(grid, row, col, i, j + 1)

class Solution:
    def num(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        cnt = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    self.dfs(i, j, grid)
                    cnt +=1

        for k in grid:
            print(k)
        return cnt
    def dfs(self,i, j, grid):
        print(i,j )
        for k in grid:
            print(k)
        print("will chang",i,j )
        print()
        grid[i][j]="X"

        if i - 1>= 0 and grid[i-1][j]=="1":
            self.dfs(i-1, j, grid)
        if i + 1< len(grid) and grid[i +1][j]=="1":
            self.dfs(i + 1, j, grid)
        if j - 1 >= 0 and grid[i][j-1] =="1":
            self.dfs(i, j -1, grid)
        if j + 1 < len(grid[0]) and grid[i][j+1]=="1":
            self.dfs(i,j + 1, grid)


if __name__ == '__main__':
    grid=[["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","1"]]

    print(Sol().num(grid))