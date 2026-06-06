import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      result= defaultdict(list)
      for s in strs:
        idx=[0]*26
        for ch in s:
            chs= ord(ch)-ord('a')
            idx[chs]+=1
        result[tuple(idx)].append(s)
      return list(result.values())

      