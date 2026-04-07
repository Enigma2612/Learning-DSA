class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs2 = {}
        for ind, i in enumerate(strs):
            letter_lis = [0]*26
            for j in i:
                letter_lis[ord(j)-97] += 1
            
            strs2[tuple(letter_lis)] = strs2.get(tuple(letter_lis), []) + [i]
        
        return list(strs2.values())

#Time: O(26 * N * M) (M -> max len of string in strs, N -> len of strs)
#Space: O(N)