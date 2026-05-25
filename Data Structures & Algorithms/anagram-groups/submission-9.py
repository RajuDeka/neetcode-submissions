class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for i in strs:
            a = [0]*26
            for j in i:
                a[ord(j)-ord('a')]  += 1
            key = tuple(a)
            hm[key].append(i)
        return list(hm.values())