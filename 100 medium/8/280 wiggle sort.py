"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

"""


class Solution:
    def wiggle(self, nums):
        for i in range(len(nums)):
            if ((i % 2) and nums[i] < nums[i - 1]) or (not (i % 2) and nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]


if __name__ == '__main__':
    nums = [3, 1, 4, 2, 6, 5]
    Solution().wiggle(nums)
    print(nums)
