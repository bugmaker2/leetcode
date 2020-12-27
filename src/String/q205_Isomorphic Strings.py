class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1 = dict()
        hashmap2 = dict()
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False
        for i in range(slen):
            if not(s[i] in hashmap1):
                hashmap1[s[i]] = t[i]
            if hashmap1[s[i]] != t[i]:
                return False
            if not(t[i] in hashmap2):
                hashmap2[t[i]] = s[i]
            if hashmap2[t[i]] != s[i]:
                return False
        return True
