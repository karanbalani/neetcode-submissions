class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ss = ''.join(sorted([c for c in s]))
        st = ''.join(sorted([c for c in t]))

        return ss == st