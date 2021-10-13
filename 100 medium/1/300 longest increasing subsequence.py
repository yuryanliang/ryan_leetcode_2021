""" https://leetcode.com/problems/longest-increasing-subsequence/
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

"""
这种解法的时间复杂度为O(n2)，类似brute force的解法，我们维护一个一维dp数组，
其中dp[i]表示以nums[i]为结尾的最长递增子串的长度，对于每一个nums[i]，
我们从第一个数再搜索到i，如果发现某个数小于nums[i]，我们更新dp[i]，
更新方法为dp[i] = max(dp[i], dp[j] + 1)，即比较当前dp[i]的值和那个小于num[i]的数的dp值加1的大小，
我们就这样不断的更新dp数组，到最后dp数组中最大的值就是我们要返回的LIS的长度，参见代码如下："""

# Time:  O(n^2)
# Space: O(n)
# Traditional DP solution.
class Sol:
    def dp(self, nums):
        dp = [1 for i in range(len(nums))] # dp[i] is the length of LIS ends with nums[i]
        for i in range(len(nums)):
            # dp.append(1)
            for j in range(i):
                if nums[j] <nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

    # https: // medium.com / swlh / a - visual - guide - to - solving - the - longest - increasing - subsequence - problem - dabbee570551


# Binary search solution.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []

        def insert(target):
            left, right = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while left <= right:
                mid = left + (right - left) // 2
                if LIS[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target)
            else:
                LIS[left] = target

        for num in nums:
            insert(num)

        return len(LIS)