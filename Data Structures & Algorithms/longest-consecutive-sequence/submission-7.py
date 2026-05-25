class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        longest = 0
        for i in nums:
            if (i-1) not in hs:
                length = 0
                while (i+length) in hs:
                    length += 1
                longest = max(length,longest)
        return longest
