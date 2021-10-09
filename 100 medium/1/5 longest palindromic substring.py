""" https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

"""
每个字母为中心loop一遍

内层while 循环同时向两边扩展

分 single 和double 两种情况
"""
'cab'
class Sol:
    def longest(self, s):
        res = ''
        for i in range(len(s)):
            odd =  self.palindromeAt(s, i , i)
            even = self.palindromeAt(s, i , i + 1)

            res = max(res, odd, even, key=len)
        return res
    def palindromeAt(self, s, l, r): # start from left, right index expand outwards to find the longest palindrome
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r ]

