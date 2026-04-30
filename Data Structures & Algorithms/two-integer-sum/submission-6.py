class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i,num in enumerate(nums):
            res = target - num
            if res in hs:
                return [hs[res],i]
            hs[num] = i

