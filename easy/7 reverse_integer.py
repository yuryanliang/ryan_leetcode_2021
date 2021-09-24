"""Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

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
        n = x if x > 0 else -x  # need to change to n, otherwise the lower x sign check, x will be 0
        res = 0
        while n:
            res = res * 10 + n % 10
            n = n // 10
        if res > 0x7fffffff:
            return 0
        else:
            return res if x > 0 else -res


def main():
    x = -123
    print(Solution().reverse(x))


if __name__ == "__main__":
    main()
