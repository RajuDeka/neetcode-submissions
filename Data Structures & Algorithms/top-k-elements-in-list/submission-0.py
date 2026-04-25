class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = defaultdict(int)
        for i in nums:
            hs[i] += 1
        
        b = [ [] for _ in range(len(nums) + 1)]
        for num,count in hs.items():
            b[count].append(num)

        res = []
        for i in range(len(b)-1,0,-1):
            for num in b[i]:
                res.append(num)
            if len(res) == k:
                return res