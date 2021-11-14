""" https://leetcode.com/problems/ransom-note/
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
class Solution:
    def canConstruct(self, ransomNote, magazine):
        lookup = {}
        for c in magazine:
            if c in lookup:
                lookup[c] +=1
            else:
                lookup[c] = 1

        for c in ransomNote:
            if c in lookup:
                lookup[c]-=1
                if lookup[c] <0:
                    return False
            else:
                return False
        return True

if __name__ == '__main__':
    note="aa"
    mag = "aab"
    print(Solution().canConstruct(note, mag))