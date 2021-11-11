"""
Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]

"""
class Solution:
    def missingRanges(self, nums, lower, upper):
        def get_range(start, end):
            if start == end:
                return str(start)
            else:
                return str(start) + "->" + str(end)

        res = []
        pre = lower - 1

        for i in range(len(nums) + 1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]

            if cur - pre >=2:
                res.append(get_range(pre+1, cur -1))
            pre = cur
        return res


if __name__ == '__main__':
    nums=[0, 1, 3, 50, 75]
    nums= [3, 4, 5, 90]
    print(Solution().missingRanges(nums, 0, 99))