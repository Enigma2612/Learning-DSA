#Problem: Reverse a given array IN PLACE

#My take (Solution 1)
def reverse(arr, N):
    if N == 1:
        return
    reverse(arr, N-1)
    arr.append(arr[len(arr) - N])
    arr.pop(len(arr) - N - 1)
    