""" https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

We define a mid variable (line #8, this way of defining mid is to prevent overflow problem, you don't need to worry about this.
mid = (low + high) /2 or mid = (low + high) //2 or mid = (low + high) >> 1 also works) and compare it with target (line #9).
If it's the target, update the index variable (line #10). However, we're not done here. Think about this example [1,3,3,3,5]. mid is 3 here.
But, it's not the left most 3, is it? So, you update index but at the same time, try to move to the left side of mid to find the left most target value
(line #11, for the findEndingIndex function, you want to move to the right of mid, so you make low = mid + 1, line #16), 3 in this example. Make sense? Good.
"""


class Solution:
    def searchRange(self, nums, target):
        start = self.binarySearchFindPos(nums, target)
        end = self.binarySearchFindPos(nums, target, find_start=False)
        return [start, end]

    def binarySearchFindPos(self, nums, target, find_start=True):
        left = 0
        right = len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
                if find_start:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return res


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
