class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        t_map = set()
        t_count = {}
        for i in t:
            t_map.add(i)
            t_count[i] = t_count.get(i, 0) + 1
    
        l = 0

        s_count = {}
        s_map = set()

        ans = ""

        def check(small,big):
            for i in small:
                if big[i] < small[i]:
                    return False
            return True

        for i in range(len(s)):
            if s[i] in t_map:
                s_map.add(s[i])
                s_count[s[i]] = s_count.get(s[i], 0) + 1
            while t_map == s_map and check(t_count, s_count):
                if (not ans) or (len(ans) > i - l + 1):
                    ans = s[l: i+1]
                if s[l] in t_map:
                    s_count[s[l]] -= 1
                    if not s_count[s[l]]:
                        s_map.remove(s[l])
                l += 1

        return ans

#Watch video to get more optimal solution, but this is pretty good