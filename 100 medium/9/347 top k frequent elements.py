""" https://leetcode.com/problems/top-k-frequent-elements/
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        d = Counter(nums)
        return sorted(d, key=d.get, reverse=True)[:k]

    def topKFrequent_1(self, nums, k):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return sorted(d, key=d.get, reverse=True)[:k]

    def topKFrequent_2(self, nums, k):
        from collections import Counter
        import heapq
        c = Counter(nums)
        return heapq.nlargest(k, c, key=c.get)
