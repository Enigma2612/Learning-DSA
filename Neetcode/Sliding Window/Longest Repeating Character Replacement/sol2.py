class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not len(s): return 0
        counter = {s[0]:1}
        ans = 1
        l = 0
        most_freq = 1

        for i in range(1, len(s)):
            c = counter.get(s[i], 0) + 1
            counter[s[i]] = c
            most_freq = max(most_freq, c)
            while (i - l + 1) - most_freq > k and l <= i:
                counter[s[l]] -= 1
                l += 1
                print(s[l:i+1])

            ans = max(ans, i - l + 1)
        
        return ans

#BEAUTIFUL OPTIMIZATION
#THE MOST FREQUENT ELEMENT DOESN'T HAVE TO BE UPDATED BECAUSE THAT WOULD DECREASE THE MAX LENGTH AHHHHH
#Very very interesting, teaches me to focus on what exactly we care about
#I don't need to know the accurate length of each substring, I just need to know the maximum it can reach
                