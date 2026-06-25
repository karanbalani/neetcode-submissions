class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for c in s:
            if c not in seen.keys():
                seen[c] = 1
                continue
            
            seen[c] += 1

        for c in t:
            if c not in seen.keys():
                return False
            
            if seen[c] == 1:
                del seen[c]
            else:
                seen[c] -= 1
            
        if len(seen.keys()) > 0:
            return False
        
        return True
