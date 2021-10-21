"""https://leetcode.com/problems/sort-colors/
Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

"""
"""
两个指针从左， 右， 表面放置最左球，和最右颜色球的起始点。
用cur指针去loop一遍球，左球放左指针， 右球放右指针， 
edge 左边要加一， 右边不用

"""

class Solution:
    def sortColors(self, nums):
        left = 0
        cur = 0
        right = len(nums) - 1

        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                cur += 1
                left += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            else:
                cur += 1

    def select_sort(self, nums):
        for i in range(nums):
            min_index = i
            for j in range(i + 1, nums):
                if nums[min_index] >nums[j]:
                    min_index = j
            nums[min_index], nums[i]= nums[i], nums[min_index]



if __name__ == "__main__":
    A = [2, 1, 1, 0, 0, 2]
    Solution().sortColors(A)
    print(A)

