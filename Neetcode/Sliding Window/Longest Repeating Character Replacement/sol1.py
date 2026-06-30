class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not len(s): return 0
        counter = {s[0]:1}
        ans = 1
        l = 0

        for i in range(1, len(s)):
            c = counter.get(s[i], 0) + 1
            counter[s[i]] = c
            most_freq = max(counter.values())
            while (i - l + 1) - most_freq > k and l <= i:
                counter[s[l]] -= 1
                l += 1
                most_freq = max(counter.values())
                print(s[l:i+1])

            ans = max(ans, i - l + 1)
        
        return ans

#Very interesting problem

