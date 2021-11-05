"""Time:  O(n * s), s is the sum of nums
Space: O(s)

Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.

Note:
Both the array size and each of the array element will not exceed 100.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)  # dp[i]表示原数组是否可以取出若干个数字，其和为i
        # 那么我们最后只需要返回dp[target]就行了
        dp[0] = True

        for num in nums:
            for i in reversed(range(num, target + 1)):
                rest = i - num
                rest_if_can = dp[i-num]
                dp[i] = dp[i] or rest_if_can
        return dp[target]

if __name__ == '__main__':
    # for i in range(5, 0, -1):
    #     print(i)
    # print("____________")
    # for i in reversed(range(1, 6)):
    #     print(i)

    nums = [1, 2, 3, 4]
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # nums = [1, 2, 5]

    print(Solution().canPartition(nums))