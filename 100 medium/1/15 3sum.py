""" https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
方法一：
用for loop 循环第三个值， 另两个值做 two sum

方法二；
sort 数组
while loop 循环第三个值， 另两个值 用双指针从左右向中间移动
注意 符合条件之后的移动 要dedup
"""

class Sol:
    def three_sum(self, nums):
        res = []
        for i in range(len(nums)):
            # 2 sum
            target =  0 - nums[i]
            lookup = {}
            for j in range(i + 1, len(nums)):
                if target - nums[j] in lookup:
                    sol = [nums[i], nums[j], target - nums[j]]
                    sol.sort()
                    if sol not in res:
                        res.append(sol)
                else:
                    lookup[nums[j]] = j
        return res


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            target = 0 - nums[i]
            lookup = {}
            for j in range( i + 1, len(nums)):
                if target - nums[j] in lookup:
                    val = [nums[i], nums[j], target- nums[j]]
                    val.sort()
                    if val not in res:
                        res.append(val)
                else:
                    lookup[nums[j]]= j
            return res