""" https://leetcode.com/problems/jump-game-ii/
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""
class Solution:
    def jump(self, nums):
        edge = 0
        maxEdge = 0
        cnt = 0

        for i in range(len(nums)):
            if i > edge: # when you need to jump to get to index i, because i > cur edge
                edge= maxEdge
                cnt+=1
            maxEdge= max(maxEdge, i + nums[i])
        return cnt

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))