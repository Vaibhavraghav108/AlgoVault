class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            result="".join(sorted(i))
            if result in dict:
                dict[result].append(i)
            else:
                dict[result]=[i]
        return list(dict.values())