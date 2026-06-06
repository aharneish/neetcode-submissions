class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict=defaultdict(list)
        for word in strs:
            key=''.join(sorted(word))
            map_dict[key].append(word)
        return list(map_dict.values())