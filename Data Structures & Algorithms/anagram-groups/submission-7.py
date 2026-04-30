class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        
        for i in strs:
            ar = [0] * 26
            for j in i:
                ar[ord(j)-ord('a')] += 1
            key = tuple(ar)
            hs[key].append(i)
        return list(hs.values())