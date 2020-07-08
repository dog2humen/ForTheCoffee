class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k == 0: return []
        elif shorter == longer: return [k*shorter]
        else: return [(k-i)*shorter + i*longer for i in range(k+1)]
