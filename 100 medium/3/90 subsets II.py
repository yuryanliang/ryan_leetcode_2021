""" https://leetcode.com/problems/subsets-ii/
Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

"""
用i + 1， 而不是ind 加一。来略过已经用过的值
"""

class Solution:
    def subsetWithDup(self, nums):
        res = []
        path = []
        ind = 0
        self.help(nums, res, path, ind)
        return res
    def helper(self, nums, res, path, ind):
        temp = list(path)
        temp.sort()
        if temp not in res:
            res.append(temp)

        for i in range(ind, len(nums)):
            path.append(nums[i])
            self.helper(nums, res, path, i + 1)
            path.pop()

def main():
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))


if __name__ == '__main__':
    main()