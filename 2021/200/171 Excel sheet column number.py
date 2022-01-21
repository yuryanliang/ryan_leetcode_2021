"""https://leetcode.com/problems/excel-sheet-column-number/
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
"""
class Solution:
    def titleToNumber(self, s):
        result = 0
        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1
        return result

if __name__ == '__main__':
    columnTitle = "AB"
    print(Solution().titleToNumber(columnTitle))
