"""
This is a follow up of Shortest Word Distance.
The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters.
 How would you optimize it?

Design a class which receives a list of words in the constructor,
and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
class Solution:
    def __init__(self, words):
        self.words = words
        from collections import defaultdict
        self.lookup = defaultdict(list)
        for i, val in enumerate(words):
            self.lookup[val].append(i)

    def distance(self, word1, word2):
        dist = len(self.words) + 1
        index1 = self.lookup[word1]
        index2  = self.lookup[word2]

        i=j = 0
        while i <len(index1) and j <len(index2):
            dist = min(dist, abs(index1[i]-index2[j]))
            if index1[i]< index2[j]:
                i +=1
            else:
                j +=1
        return dist
if __name__ == '__main__':
    words = ["i", "a", "i", "b", "a"]
    word1 = "a"
    word2 = "b"
    print(Solution(words).distance(word1, word2))