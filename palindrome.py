class Solution:
    """ We can use just str , without turple , and also if is not necessary  """
    def isPalidrome(self, x: int) -> bool:
        t = tuple(str(x))
        p_t = t[::-1]
        if t == p_t:
            return True
        return False



pol = Solution()

pol.isPalidrome(121)

