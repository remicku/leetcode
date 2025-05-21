class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
        prev = 1

        for i in range(1, n + 1):
            if i == prev * 2:
                prev = i

            ans[i] = 1 + ans[i - prev]

        return ans
        