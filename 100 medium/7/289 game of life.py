""" https://leetcode.com/problems/game-of-life/
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""


# https://leetcode.com/problems/game-of-life/discuss/1534757/Python-solution-using-2-approaches-with-explanation

class Solution:
    def gameOfLife(self, board):
        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return
            if i < 0 or i > len(board) - 1:
                return
            if j < 0 or j > len(board[0]) - 1:
                return

            cnt = 0

            if i > 0 and board[i - 1][j]:  # up
                cnt += 1
            if j > 0 and board[i][j - 1]:  # left
                cnt += 1
            if i < len(board) - 1 and board[i + 1][j]:  # down
                cnt += 1
            if j < len(board[0]) - 1 and board[i][j + 1]:  # right
                cnt += 1
            if i > 0 and j > 0 and board[i - 1][j - 1]:  # up left
                cnt += 1
            if i > 0 and j < len(board[0]) - 1 and board[i - 1][j + 1]:  # up right
                cnt += 1
            if i < len(board) - 1 and j > 0 and board[i + 1][j - 1]:  # down left
                cnt += 1
            if i < len(board) - 1 and j < len(board[0]) - 1 and board[i + 1][j + 1]:  # down right
                cnt += 1

            visited.add((i, j))

            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j - 1)
            dfs(i - 1, j + 1)
            dfs(i + 1, j - 1)
            dfs(i + 1, j + 1)

            if board[i][j]:
                if cnt < 2 or cnt > 3:
                    board[i][j] = 0
            else:
                if cnt == 3:
                    board[i][j] = 1

        dfs(0, 0)

    def gameOfLife1(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0

                if i > 0 and board[i - 1][j] > 0: count += 1
                if j > 0 and board[i][j - 1] > 0: count += 1
                if i < len(board) - 1 and board[i + 1][j] > 0: count += 1
                if j < len(board[0]) - 1 and board[i][j + 1] > 0: count += 1
                if i > 0 and j > 0 and board[i - 1][j - 1] > 0: count += 1
                if i > 0 and j < len(board[0]) - 1 and board[i - 1][j + 1] > 0: count += 1
                if i < len(board) - 1 and j > 0 and board[i + 1][j - 1] > 0: count += 1
                if i < len(board) - 1 and j < len(board[0]) - 1 and board[i + 1][j + 1] > 0: count += 1

                if board[i][j]:
                    if count < 2 or count > 3: board[i][j] = 2
                else:
                    if count == 3: board[i][j] = -1
        # Replacing 2 with 0 and -1 with 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2: board[i][j] = 0
                if board[i][j] == -1: board[i][j] = 1


if __name__ == '__main__':
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    # print(Solution().check(board, 2, 0))
    print(Solution().gameOfLife(board))
