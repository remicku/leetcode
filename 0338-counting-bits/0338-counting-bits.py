class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        prev = 1

        for i in range(1, n + 1):
            if i == prev * 2:
                prev = i

            ans.append(1 + ans[i - prev])

        return ans
        