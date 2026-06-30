class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        longest = 1
        current = 1
        l = 0
        cur_map = {s[0]}
        for i in range(1, len(s)):
            print(cur_map)
            while s[i] in cur_map:
                cur_map.remove(s[l])
                l += 1
            else:
                cur_map.add(s[i])
                current = i - l + 1
                longest = max(longest, current)
        return longest

#nice problem, made me realize that using a sliding window is slightly less naturally obvious to me