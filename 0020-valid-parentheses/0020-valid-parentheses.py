class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = {'(':')', '{':'}', '[':']'}

        for c in s:
            if c in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False

                p = stack.pop()

                if c != hashmap[p]:
                    return False
                
        return not stack
