class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {} # sorted word : list

        for word in strs:

            sword = "".join(sorted([c for c in word]))

            ltu = [] # list to update
            if sword in hmap.keys():
                ltu = hmap.get(sword, [])
            
            ltu.append(word)
            hmap[sword] = ltu

        return list(hmap.values())