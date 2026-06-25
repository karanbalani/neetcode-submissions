class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        htoidx = {} # sorted string to indexes

        for idx, word in enumerate(strs):
            s = "".join(sorted([c for c in word]))
            
            if s not in htoidx:
                htoidx[s] = list()
                
            
            htoidx[s].append(idx)

        
        output = []

        for key in htoidx.keys():
            temp = []
            for idx in htoidx[key]:
                temp.append(strs[idx])
            output.append(temp)
        
        return output