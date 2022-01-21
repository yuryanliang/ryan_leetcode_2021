"""https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
"""
class Solution:
    def majorityElement(self, nums):
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
            if dict[num] > len(nums)//2:
                return num
if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums))
