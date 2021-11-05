""" https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
class Solution:
    def generateParentheses(self, n):
        res = []
        path = ""
        left = 0
        right = 0
        self.dfs(n, res, path, left, right)
        return res
    def dfs(self, n, res, path, left, right):
        if len(path) == n * 2:
            res.append(path)
        else:
            if left < n:
                self.dfs(n, res, path + "(", left + 1, right)
            if right < left:
                self.dfs(n, res, path + ")", left, right + 1)

if __name__ == "__main__":
    print(Solution().generateParentheses(3))