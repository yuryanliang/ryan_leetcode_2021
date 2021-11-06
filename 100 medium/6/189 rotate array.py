""" https://leetcode.com/problems/rotate-array/
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
class Solution:
    def rotate(self, nums, k):
        k %= len(nums)

        for _ in range(k):
            previous = nums[-1]
            for i in range(len(nums)):
                previous, nums[i] = nums[i], previous
    def rotate_1(self, nums, k):
        if k > len(nums):
            k %= len(nums)
        first = nums[-k:]
        second = nums[:-k]
        nums[:k] = first
        nums[k:] = second

    def rotate_2(self, nums, k):
        while k:
            nums.insert(0, nums.pop())
            k -= 1
    def rotate_3(self, nums, k):
        from collections import deque
        d = deque(nums)
        for _ in range(k):
            d.appendleft(d.pop())
        nums[:] = list(d)
    def rotate_4(self, nums, k):
        k %= len(nums)
        count, start = 0, 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while 1:
                current = (current + k) % len(nums)
                temp, nums[current] = nums[current], prev
                prev = temp
                count += 1
                if start == current:
                    break
            start += 1

    def rotate1(self, nums, k):
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

if __name__ == '__main__':
    # nums =[1,2,3,4,5,6,7]
    # k = 3
    # nums =[1]
    # k = 0
    nums =[1, 2]
    k = 3
    Solution().rotate_2(nums, k)
    print(nums)