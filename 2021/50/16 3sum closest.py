""" https://leetcode.com/problems/3sum-closest/
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0


Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) -2):
            j = i + 1
            k = len(nums) -1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == target:
                    return sum3
                if abs(sum3 - target) < abs(res - target):
                    res = sum3
                if sum3 < target:
                    j +=1
                elif sum3 > target:
                    k -= 1
        return res
if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))
