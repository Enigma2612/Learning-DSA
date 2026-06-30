class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = {}
        for i in s1: s1_map[i] = s1_map.get(i, 0) + 1


        size = len(s1)

        cur_map = {}

        for i in range(0, size):
            cur_map[s2[i]] = cur_map.get(s2[i], 0) + 1
        if cur_map == s1_map:
                return True
        for i in range(size, len(s2)):
            prev = s2[i-size]
            cur_map[prev] -= 1
            if not cur_map[prev]: del cur_map[prev]
            cur_map[s2[i]] = cur_map.get(s2[i], 0) + 1
            if cur_map == s1_map:
                return True
            print(cur_map)
            
        return False
            

#Watch vid, might get a better solution   
        