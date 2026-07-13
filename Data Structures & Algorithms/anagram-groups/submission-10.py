class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            result="".join(sorted(i))
            if result not in dict:
                dict[result]=[]
            dict[result].append(i)
        return list(dict.values())