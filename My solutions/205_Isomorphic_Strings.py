class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        hashset = set()
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashset:
                    return False
            elif hashmap[s[i]] != t[i]:
                return False
            hashmap[s[i]] = t[i]
            hashset.add(t[i])

        return True