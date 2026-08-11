class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1,set2 = {},{}
        for i in s:
            if i in set1:
                set1[i] += 1
            else:
                set1[i] = 1
        for i in t:
            if i in set2:
                set2[i] += 1
            else:
                set2[i] = 1
        return set1 == set2