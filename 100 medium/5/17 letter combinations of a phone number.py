"""

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""
"""
DFS 中 什么时候用if else; 什么时候用 if return?
如果用了if else 就不用return。 用了return， 就不用else

DFS 中 什么时候用pop?
如果path是list， 需要用 append 加新元素， 不能把append 和 dfs 写在一行时候，要单调用pop
如果path是string， 可以直接在dfs一行处理，就不用pop

https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/780232/Backtracking-Python-problems%2B-solutions-interview-prep

"""


# backtrack
class Solution:
    def letterCombinations(self, digits):
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        if not digits:
            return res
        index = 0
        path =''
        self.dfs(digits, index, dic, path, res )
        return res

    def dfs(self, digits, index, dic, path, res):
        if index >= len(digits):
            res.append(path)
            return

        string1= dic[digits[index]]
        for i in string1:
            self.dfs(digits, index + 1, dic, path + i, res)
if __name__ == '__main__':
    digits = "23"
    print(Solution().letterCombinations(digits))