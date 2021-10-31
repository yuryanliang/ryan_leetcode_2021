""" https://leetcode.com/problems/product-of-array-except-self/
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)

"""
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        fwd = [1 for _ in range(n)]
        bwd = [1 for _ in range(n)]
        res = [1 for _ in range(n)]

        for i in range(1, n):
            fwd[i] = fwd[i -1] * nums[i -1]
        for j in range(n-2, -1, -1):
            bwd[j] = bwd[j + 1] * nums[j + 1]
        for k in range(n):
            res[k] = fwd[k] * bwd[k]
        return res

    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
if __name__ == '__main__':
    for i in range( 3, -1, -1):
        print(i)
    nums = [1, 2, 3, 4]
    # print(Solution().productExceptSelf(nums))