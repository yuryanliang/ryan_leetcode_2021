""" https://leetcode.com/problems/sqrtx/
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
class Sol:
    def brute_force(self, x):
        i = 0
        while i ** 2 <= x:
            i += 1
        i = i -1
        return i

    def binary_search(self, x):
        left = 0
        right = x

        while left < right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left -1

    def amazon(self, x):
        if x < 2:
            return x
        left = 0
        right = x
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        i = left -1

        small = (i ** 2) - x
        big = ((i+1) ** 2) - x
        return i if abs(small) < abs(big) else i + 1
