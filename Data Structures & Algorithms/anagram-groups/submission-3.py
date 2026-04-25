class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            hs[key].append(i)
        return list(hs.values())

        