class Solution:
    def isPalindrome(self, s: str) -> bool:
        x, y = 0, len(s) - 1

        while x < y:

            # skip any spaces from left and right
            while x < y and not s[x].isalnum():
                x += 1
            
            while x < y and not s[y].isalnum():
                y -= 1
            
            # quick return
            if s[x].lower() != s[y].lower():
                return False
            
            x += 1
            y -= 1
            
        
        return True