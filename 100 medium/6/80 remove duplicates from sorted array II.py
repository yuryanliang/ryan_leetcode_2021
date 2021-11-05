"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question.

"""
class Solution:
    def removeDuplicates(self, nums):
        slow = 0
        fast = 1
        cnt = 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                cnt = 1
            elif cnt < 2:
                slow += 1
                nums[slow] = nums[fast]
                cnt += 1
            fast += 1
        return slow + 1

if __name__ == '__main__':
    # nums =[1,1,1,2,2,3]
    nums=[1, 2,2]
    # nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

    print(Solution().removeDuplicates(nums))