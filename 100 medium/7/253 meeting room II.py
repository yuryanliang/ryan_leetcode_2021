"""
Given an array of meeting time intervals consisting of
start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019.
 Please reset to default code definition to get new method signature.
"""
class Solution:
    def meeting(self, intervals):
        start = end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])

        start.sort()
        end.sort()

        s = e = 0
        min_room = cnt_room = 0

        while s < len(start):
            if start[s] < end[e]:
                cnt_room +=1
                min_room= min(min_room , cnt_room)
                s +=1
            else:
                cnt_room -=1
                e +=1
        return min_room