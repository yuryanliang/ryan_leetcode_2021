"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list
"""

class Solution:
    def distance(self, words, word1, word2):
        last_w1 = last_w2 = -1
        i = 0
        dist = len(words) + 1
        while i < len(words):
            if words[i] == word1:
                last_w1 = i
            elif words[i] == word2:
                last_w2 = i
            if last_w1 >= 0 and last_w2 >= 0:
                dist = min(dist, abs(last_w1 - last_w2))
            i += 1
        return dist

if __name__ == '__main__':
    words = ["i", "a", "i", "b", "a"]
    word1 = "a"
    word2 = "b"
    print(Solution().distance(words, word1, word2))