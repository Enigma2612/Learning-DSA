#Problem: Reverse a given array IN PLACE

#My take (Solution 1)
def reverse(arr, N):
    if N == 1:
        return
    reverse(arr, N-1)
    arr.append(arr[len(arr) - N])
    arr.pop(len(arr) - N - 1)

#IMPORTANT: Issue here: Popping from the middle of the list, is O(N)! 
#So Time complexity becomes O(N^2), because of the popping step
#I'll try to use element swapping somehow, instead of using insertion / deletion
    