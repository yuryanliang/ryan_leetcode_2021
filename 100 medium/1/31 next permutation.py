""" https://leetcode.com/problems/next-permutation/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
"""
"""
找最后一个单调递减区间，  1,3,2
区间的前一个点就是 pivot  1
把pivot 和 最后面数起， 第一个大于pivot的值交换 2
把原单调递减区间sort 2,1,3

edge case：
找不到pivot 原函数递减，return 直接reverse

"""

class Sol:
    def next(self, nums):
        # Use two-pointers: two pointers start from back
        # first pointer j stop at descending point
        # second pointer i stop at value > nums[j]
        # swap and sort rest
        if not nums: return None
        i = len(nums)-1
        j = -1 # j is set to -1 for case `4321`, so need to reverse all in following step
        while i > 0:
            if nums[i-1] < nums[i]: # first one violates the trend
              j = i-1
              break
            i-=1
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] > nums[j]: #
                nums[i], nums[j] = nums[j], nums[i] # swap position
                nums[j+1:] = sorted(nums[j+1:]) # sort rest
                return