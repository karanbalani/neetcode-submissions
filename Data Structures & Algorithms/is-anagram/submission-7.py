class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ss = "".join(a for a in sorted(list(s)))
        st = "".join(a for a in sorted(list(t)))

        if ss == st:
            return True
        
        return False