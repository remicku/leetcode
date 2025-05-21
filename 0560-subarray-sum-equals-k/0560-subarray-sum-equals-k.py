class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        n = len(nums)
        prefixes = {0: 1}
        sum = 0

        for i in range(n):
            sum += nums[i]
            diff = sum - k
            res += prefixes.get(diff, 0)
            prefixes[sum] = 1 + prefixes.get(sum, 0)

        return res