class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        par = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in par:
                stack.append(c)
            else:
                if len(stack) == 0 or c != par[stack.pop()]:
                    return False

        return len(stack) == 0