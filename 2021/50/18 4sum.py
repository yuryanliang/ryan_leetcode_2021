""" https://leetcode.com/problems/4sum/
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1, n):
                target_for_two = target - nums[i] - nums[j]
                left = j + 1
                right = n - 1
                while left < right:
                    if nums[left] + nums[right] < target_for_two:
                        left +=1
                    elif nums[left] + nums[right] > target_for_two:
                        right -=1
                    else:
                        temp =[nums[i], nums[j], nums[left], nums[right]]
                        if temp not in res:
                            res.append(temp)
                        left +=1
                        right -=1
        return res

if __name__ == '__main__':
    # nums = [1, 0, -1, 0, -2, 2]
    # target = 0
    nums = [2, 2, 2, 2, 2]
    target = 8

    print(Solution().fourSum(nums, target))
