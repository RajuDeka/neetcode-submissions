class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ar = [0] * 26
        for c1,c2 in zip(s,t):
            ar[ord(c1) - ord('a')] += 1
            ar[ord(c2) - ord('a')] -= 1

        return all( i==0 for i in ar )  