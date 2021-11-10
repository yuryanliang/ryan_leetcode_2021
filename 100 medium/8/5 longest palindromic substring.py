""" https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp
            temp = self.helper(s, i , i+1)
            if len(temp) > len(res):
                res = temp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >=0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l +1: r]

if __name__ == '__main__':
    s = "babad"
    # s = "cbbd"
    # s = "a"
    print(Solution().longestPalindrome(s))