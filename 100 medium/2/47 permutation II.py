""" https://leetcode.com/problems/permutations-ii/
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

"""
因为有重复的数 ， 所以需要做一个used 的 备份表， 每次加数字之前看看有没有用过。 
从第二个开始，即（i>0)，如果后一个数跟前面的一样，并且没用过，要掠过
"""
class Sol:
    def permute(self, nums):
        res = []
        path = []
        used =[False]* len(nums)
        self.helper(nums, used, path, res)
        return res

    def helper(self,nums, used, path, res):
        if len(path) == len(nums):
            if path not in res:
                temp = path.copy()
                res.append(temp)
                return
        for i in range(len(nums)):
            if not used[i]:
                if i> 0 and nums[i -1] == nums[i] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])

                self.helper(nums, used, path, res)
                path.pop()
                used[i]= False
