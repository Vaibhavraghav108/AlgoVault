class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            target="".join(sorted(i))
            if target not in dict:
                dict[target]=[]
            dict[target].append(i)
        return list(dict.values())