#!/usr/bin/env python

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        dup_mis = []
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                count += 1
                dup_mis.append(nums[i])
                dup_mis.append(nums[i] + 1)
                return dup_mis



new = Solution()
test_nums = [1,1,3,4]
print(new.findErrorNums(test_nums))