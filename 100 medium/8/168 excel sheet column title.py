""" https://leetcode.com/problems/excel-sheet-column-title/
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""


# ord("A") = 65
# use (n-1)%26 to get 0 - 25

class Solution:
    def excel(self, n):
        res = ''

        while n:
            res += chr((n - 1) % 26 + ord('A'))
            n = (n - 1) // 26
        return res[::-1]


if __name__ == '__main__':
    n = 26
    print(Solution().excel(n))
