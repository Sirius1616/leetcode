#!/usr/bin/env python

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min_num = min(nums)
        max_num = max(nums)

        min_max = list(range(min_num, max_num+1))
        list_dis = [x for x in min_max if x not in nums]
        return list_dis


new = Solution()

print(new.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

