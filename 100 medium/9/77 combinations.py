""" https://leetcode.com/problems/combinations/
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
https://leetcode.com/problems/combinations/discuss/429526/General-Backtracking-questions-solutions-in-Python-for-reference-%3A
"""
class Solution:
    def combine(self, n , k):
        res = []
        nums = list(range(1, n +1))
        target = k
        index = 0
        path =[]
        self.helper(nums, target, index, path, res)
        return res
    def helper(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.helper(nums, target -1, i+1, path+[nums[i]], res)



if __name__ == '__main__':
    n = 3
    k = 2
    print(Solution().combine(n, k))