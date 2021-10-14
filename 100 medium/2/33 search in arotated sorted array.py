""" https://leetcode.com/problems/search-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""

"""

binary search
首先判断，是在pivot的那一段 ，按照mid值 和 left值的比较
为了方便 ，把左中右都试一遍是不是 target
然后根据中间值的位置， 将左 右 换成mid
"""

class Sol:
    def search(self, nums, target):
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) //2

            if nums[mid]  == target:
                return mid
            # inflection point to the right. Left is strictly increasing

            if nums[left] <= nums[mid]:
                if nums[left] <= target <nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            # inflection point to the left of me. Right is strictly increasing

            else:
                if nums[mid]<target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:  # edge case
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target: # test the result
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right


            if nums[0] < nums[mid]:  # ascending order before pivot point
                if nums[left] < target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:

                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid
        if nums[left] == target:
            return left
        else:
            return -1

def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    # nums = [3,1]
    # target = 1
    print(Sol().search(nums, target))


if __name__ == '__main__':
    main()