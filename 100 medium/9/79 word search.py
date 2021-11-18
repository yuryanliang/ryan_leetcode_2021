"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, i, j):
                    return True
        return False
    def helper(self, board, word, i, j):
        if len(word) == 0:
            return True

        if i <0 or i>= len(board) or j <0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False

        board[i][j] = " "

        if self.helper(board, word[1:], i+1, j):
            return True
        if self.helper(board, word[1:], i, j+1):
            return True
        if self.helper(board, word[1:], i-1, j):
            return True
        if self.helper(board, word[1:], i, j-1):
            return True

        board[i][j]= word[0]
        return False

if __name__ == '__main__':
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "SEE"
    print(Solution().exist(board, word))