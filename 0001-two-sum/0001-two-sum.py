class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hashmap = {}
        
        for i in range(n):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i