"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

input structure
[]
sorted
repeated
neg
one sol, guarantee

output
index, number
False, -1,
"""


# 时间复杂度 https://zhuanlan.zhihu.com/p/50479555
# brute force
class TwoSum:
    def two_sum(self, nums, target):
        # loop
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # edge case, len(nums) < 2, no result
        return -1

    def two_sum_dist(self, nums, target):
        lookup = {}
        for i in range(len(nums)):
            if target - nums[i] in lookup:
                return [lookup[target-nums[i]], i]
            else:
                lookup[nums[i]] = i
    def two_sum_dist_1(self, nums, target):
        lookup = {}
        for i, val in enumerate(nums):
            if target - val in lookup:
                return [lookup[target - val], i]
            else:
                lookup[val] = i

def main():
    nums = [4, 2, 1]
    target = 6
    print(TwoSum().two_sum_dist(nums, target))

if __name__== "__main__":
    main()