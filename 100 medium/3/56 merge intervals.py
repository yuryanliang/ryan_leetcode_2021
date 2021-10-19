""" https://leetcode.com/problems/merge-intervals/
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
"""
把数组按照第一个数字大小sort。 inter.sort(key=lambda x : x[0])

把每个数组和之前的比较 头尾 两个数字， 取最大，最小，重新设置数组。 注意放一个【】占位， 保证数组个数不变

最后结果dedup
"""
class Solution:
    def merge(self, intervals):
        inter = intervals
        inter.sort(key = lambda x:x[0]) # 按照第一个数 sort

        for i in range(1, len(inter)):
            if inter[i][0] <= inter[i-1][-1] and inter[i][-1] >= inter[i-1][0]:
                new_start = min(inter[i][0], inter[i-1][0])
                new_end = max(inter[i][-1], inter[i - 1][-1])

                del inter[i]
                del inter[i -1]
                inter.insert(i-1, [new_start, new_end])
                inter.insert(i -1, [-1]) #   放一个占位， 保证个数不变
        res = []
        for i in inter:
            if i not in res and i !=[-1]:
                res.append(i)
        return res

if __name__ == "__main__":
    # print (Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

    print (Solution().merge( [[1, 4], [0, 2], [3, 5]]))

    print (Solution().merge( [[2,3],[4,5],[6,7],[8,9],[1,10]]))

