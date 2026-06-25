class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resmap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            resmap[tuple(count)].append(s)
        
        return list(resmap.values())