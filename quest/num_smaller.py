#!/usr/bin/env python

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        small_list = []
        count = 0
        for i in nums:
            for j in nums:
                if j < i:
                    count += 1
            small_list.append(count)
            count = 0
        return small_list        

smaller = Solution()

print(smaller.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))