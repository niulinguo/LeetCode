class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        if shorter == longer:
            return [k * shorter]
        if k == 1:
            return [shorter]
        resultArr = []
        for i in range(0, k + 1):
            count_shorter = k - i
            count_longer = i
            length = count_shorter * shorter + count_longer * longer
            resultArr.append(length)
        return resultArr


result = Solution().divingBoard(1, 2, 2)
print(result)
