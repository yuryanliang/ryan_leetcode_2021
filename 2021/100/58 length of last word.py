""" https://leetcode.com/problems/length-of-last-word/
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s):
        n = len(s) - 1

        while n >= 0 and s[n].isspace():
            n -= 1

        res = 0
        while n >= 0 and not s[n].isspace():
            n -= 1
            res += 1
        return res

    def length1(self, s):
        wordlist = s.split()
        if wordlist:
            return len(wordlist[-1])
        return 0
if __name__ == '__main__':
    s = "luffy is still joyboy"
    print(Solution().lengthOfLastWord(s))