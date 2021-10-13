""" https://leetcode.com/problems/find-peak-element/
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
"""
"""
 https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution 
 
 
# A python3 program to find a peak
# element element using divide and conquer
 
# A binary search based function
# that returns index of a peak element
"""


class Sol:
    def peak(self, nums):
        return self.helper(nums, 0, len(nums) - 1, len(nums))

    def helper(self, nums, left, right, n):

        mid = left + (right - left) // 2

        if (mid == 0 or nums[mid - 1] <= nums[mid]) and (mid == n - 1 or nums[mid + 1] <= nums[mid]):
            return mid
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            return self.helper(nums, left, (mid - 1), len(nums))
        else:
            return self.helper(nums, (mid + 1), right, len(nums))
