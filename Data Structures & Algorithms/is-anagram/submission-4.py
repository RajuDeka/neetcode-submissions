class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hm1 = defaultdict(int)
        hm2 = defaultdict(int)
        for i in s:
            hm1[i] += 1

        for i in t:
            hm2[i] += 1

        if hm1 == hm2:
            return True
        else: 
            return False
