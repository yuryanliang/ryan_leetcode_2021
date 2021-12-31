""" https://leetcode.com/problems/single-number-ii/
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.

https://leetcode.com/problems/single-number-ii/discuss/327103/python-Binary-solution
"""
class Solution:
    def singleNumber(self, nums):
        ans = 0
        is_neg = False
        for i in range(32):
            counter = 0
            for num in nums:
                if (num >> i) & 1:
                    counter +=1
            if counter % 3 ==1:
                ans +=pow(2, i)
                if i == 31:
                    is_neg = True
        return ans if not is_neg else ans-pow(2,32)