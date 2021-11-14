""" https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
class Solution:
    def firstUniqChar(self, s):
        from collections import Counter
        counter = Counter(s)
        for i, letter in enumerate(s):
            if counter[letter] ==1:
                return i
        return -1

    def first_1(self, s):
        for i, letter in enumerate(s):
            if s.count(letter) == 1:
                return i
        return -1
    def first_lookup(self,s):
        lookup = {}

        for ch in s:
            if ch in lookup:
                lookup[ch] +=1
            else:
                lookup[ch] =1

        for key, value in lookup.items():
            if value ==1:
                return s.index(key)
        return -1

if __name__ == '__main__':
    s = "abcabe"
    Solution().firstUniqChar(s)