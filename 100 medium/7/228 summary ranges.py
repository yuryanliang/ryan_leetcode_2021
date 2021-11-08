""" https://leetcode.com/problems/summary-ranges/
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
class Solution:
    def summaryRanges(self, nums):
        res = []
        s, temp = nums[0], nums[0]
        nums.append(-1) # add -1 at the end to address the last part of res
        for i in range(1, len(nums)):
            if temp + 1 == nums[i]:
                temp = nums[i]
            else:
                if s == temp:
                    path = str(s)
                else:
                    path = str(s) +'->' +str(temp)
                res.append(path)
                s, temp = nums[i], nums[i]

        return res
if __name__ == '__main__':
    nums =[0,1,2,4,5,7]
    # nums =[0, 2, 3, 4, 6, 8, 9]
    print(Solution().summaryRanges(nums))

