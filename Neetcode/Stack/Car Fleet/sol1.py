class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        times = [(position[i], (target - position[i])/speed[i]) for i in range(len(position))]
        stack = []
        times.sort()
        times.reverse()
        times = [t[1] for t in times]

        for t in times:
            if not stack:
                stack.append(t)
            if stack[-1] < t:
                stack.append(t)
        print(stack)       
        return len(stack)          

#Coded this on my phone while waiting before a meeting lmao``