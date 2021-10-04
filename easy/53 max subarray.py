""" https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


"""

class Sol:
    def brute_force(self, nums):
        if not nums:
            return 0
        import sys
        max_sum = -sys.maxsize
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1): # len(nums) + 1 because when nums =[1], range(1,1) doesn't go into loop
                max_sum = max(max_sum, sum(nums[i:j]))
        return max_sum

    def best(self, nums):
        new_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            new_sum = max(nums[i], new_sum + nums[i]) # give up cur vs take cur with num[i]
            max_sum =max(max_sum, new_sum)
        return max_sum
