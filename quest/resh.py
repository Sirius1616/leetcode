class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        num1 = nums[:n]
        num2 = nums[n:]
        res_zip = zip(num1, num2)
        for i, j in res_zip:
            res.append(i)
            res.append(j)

        return res