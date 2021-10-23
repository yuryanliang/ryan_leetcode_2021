"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


"""
class Solution:
    def solve(self, board):
        if not board:
            return

        row = len(board)
        col = len(board[0])

        if row > 2 and col > 2:
        # search start from the boundary:

            # start from 1st and last col
            for i in range(row):
                # 1st col
                if board[i][0] == 'O':
                    self.dfs(i, 1, board)
                # last col
                if board[i][col - 1] == 'O':
                    self.dfs(i, col -2, board)

            # start from 1st and last row
            for j in range(col):
                # 1st row
                if board[0][j] == 'O':
                    self.dfs(1, j, board)

                # last row
                if board[row - 1][j] == 'O':
                    self.dfs(row -2, j , board)

            # rewrite the inner board
            for i in range(1, row -1):
                for j in range(1, col -1):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    if board[i][j] == 'A':
                        board[i][j] = 'O'

    def dfs(self, i, j ,board):
        # hit the boundary
        if i <= 0 or i >= len(board)-1 or j <= 0 or j >= len(board[0]) -1:
            return

        # hit X
        if board[i][j] == 'X':
            return

        # hit anther A
        if board[i][j] == 'A':
            return

        if board[i][j] == 'O':
            board[i][j] = 'A'

        #search in 4 directions
        self.dfs( i + 1, j, board)
        self.dfs( i - 1, j , board)
        self.dfs( i, j - 1, board)
        self.dfs(i, j + 1, board)


if __name__ == "__main__":
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    Solution().solve(board)
    print (board)




