class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,val in enumerate(nums):
            res = target - val
            if res in hm:
                return [hm[res],i]
            hm[val] = i
        



      

                