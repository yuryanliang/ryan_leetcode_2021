'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Sol:
    def needle(self, haystack, needle):  # time limit exceeded, Time O(n*m), Space O(1)

        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1

    def needle1(self, haystack, needle):  # Time O(n*m), Space O(1)
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            l = 0
            r = len(needle) - 1
            while l <= r:
                if haystack[i + l] != needle[l]:
                    break
                if haystack[i + r] != needle[r]:
                    break
                l += 1
                r -= 1
            else:
                return i
        return -1

    def needle2(self, haystack, needle):  # space  O(m) not O(1)

        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1