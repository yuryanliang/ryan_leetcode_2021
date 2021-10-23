"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

"""
DFS/backtracking 类似permutation 
1 找到所有的拆分方案
2。 看看每个part 是不是回文
3。 整体dfs。 backtracking

注意， 在helper 里面， 当i = len（s）

"""
class Solution:
    def partitoin(self, s):
        res = []
        ind = 0
        path = []
        self.helper(s, res, path, ind)
        return res

    def helper(self, s, res, path, ind):
        if ind == len(s): # reach the end of s
            res.append(list(path))
        else:
            for j in range(ind, len(s)):
                if self.is_palindrome(s[ind: j+ 1]):
                    path.append(s[ind: j+ 1])
                    self.helper(s, res, path, j+ 1)
                    path.pop()
    def is_palindrome(self,s):
        for i in range(len(s)// 2):
            if s[i] != s[- (i + 1)]:
                return False
        return True
