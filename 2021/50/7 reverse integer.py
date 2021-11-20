""" https://leetcode.com/problems/reverse-integer/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-231 <= x <= 231 - 1
"""
class Solution:
    def reverse(self, x):
        res = 0
        if x <0:
            symbol = -1
            x = -x
        else:
            symbol =1

        while x:
            res =res *10 +x %10
            x//=10
        return 0 if res > pow(2, 31) else res * symbol
    def reverse_1(self, x):
        negFlag = 1
        if x < 0:
            negFlag = -1
            str_x = str(x)[1:]
        else:
            str_x = str(x)

        x = int(str_x[::-1])
        return 0 if x > pow(2,31) else x * negFlag

if __name__ == '__main__':
    x = 123
    print(Solution().reverse_1(x))
