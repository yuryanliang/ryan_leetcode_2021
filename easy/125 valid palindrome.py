"""

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Sol:
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isPalindrome1(self, s: str) -> bool:
        temp = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                temp += c
        temp = temp.lower()

        if temp == temp[::-1]:
            return True
        else:
            return False

    def isPalindrome2(self, s: str) -> bool:
        temp = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                temp += c
        temp = temp.lower()

        l = 0
        r = len(temp) - 1

        while l < r:
            if temp[l] != temp[r]:
                return False
            l += 1
            r -= 1
        return True
