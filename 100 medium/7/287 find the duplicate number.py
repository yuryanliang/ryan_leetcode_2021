""" https://leetcode.com/problems/find-the-duplicate-number/
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
 prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
 find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution:
    def findDuplicate(self, nums):
        from collections import defaultdict
        lookup = defaultdict(list)
        for i, val in enumerate(nums):
            if val in lookup:
                return val
            else:
                lookup[val].append(i)
    def findDuplicate1(self, nums):
        left = 0
        right = len(nums) -1

        while left < right:
            mid = (left + right) // 2
            cnt = 0

            for n in nums:
                if n <= mid:
                    cnt +=1
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    nums = [1, 1, 2]

    print(Solution().findDuplicate1(nums))