class Solution:

    def encode(self, strs: list[str]) -> str:
        full_string = ''.join(strs)
        n = str(len(strs))
        lens = '[' + ''.join([f"{len(s)} " for s in strs]) + ']' + n
        full_string += lens
        return full_string
        

    def decode(self, s: str) -> list[str]:
        full_string = s
        lis = []
        #reading length of strs list
        p = -1
        while full_string[p].isnumeric():
            p -= 1
        else:
            p += 1
    
        num = int(full_string[p:])

        #finding the lengths of indiv characters
        p -= 1
        p0 = p
        while full_string[p] != '[':
            p -= 1
        
        lens = list(map(int, full_string[p+1:p0].split()))

        pointer = 0
        for l in lens:
            lis.append(full_string[pointer:pointer+l])
            pointer += l
        return(lis)

s = Solution()