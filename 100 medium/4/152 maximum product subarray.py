""" https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


"""
local max, local min 需要同时在一行计算
"""
class Solution:
    def maxProduct_dp(self, nums):
        prev_max = nums[0]
        prev_min = nums[0] # min in previous iteration
        max_to_n = nums[0] # max this iteration
        min_to_n = nums[0]
        ans = nums[0]

        for i in nums[1:]:
            # two negative can be positive
            max_to_n = max(max(prev_max * i, prev_min * i), i)
            min_to_n = min(min(prev_max * i, prev_min * i), i)
            prev_max = max_to_n
            prev_min = min_to_n
            ans = max(ans, max_to_n)
        return ans





if __name__ == "__main__":
    print (Solution().maxProduct_dp([0, 2]))
    # print (Solution().maxProduct_1([2, 3, -2, 4]))
    # print (Solution().maxProduct([-4,-3]))