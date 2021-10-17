"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]



测试地址：
https://leetcode.com/problems/subsets/description/

"""

"""
要把每个结果sort 再加入res
permutation + 控制长度 + sort
"""

class Sol:
    def subset(self, nums):
        if not nums:
            return []
        res = [[]]
        path = []
        start = 0
        self.helper(nums, start, path, res)
    def helper(self, nums, start, path, res):
        temp = path.copy()
        temp.sort()
        if temp not in res:
            res.append(temp)

        for i in range(start, len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                self.helper(nums, start + 1 , path, res)
                path.pop()