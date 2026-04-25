class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = defaultdict(int)
        for i in nums:
            hs[i] += 1
        
        freq = [ [] for _ in range(len(nums) + 1)]
        for i,num in hs.items():
            freq[num].append(i)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
