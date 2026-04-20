class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = {}
        for i in nums:
            if i in hs:
                return True
            else:
                hs[i] = i
        return False
