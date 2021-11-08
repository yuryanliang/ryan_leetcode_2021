"""
Given an array of meeting time intervals consisting
of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""


class Solution:
    def meeting(self, intervals):
        intervals.sort(key = lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True


if __name__ == '__main__':
    intervals=[[0, 30],[15, 20],[5, 10]]
    print(Solution().meeting(intervals))