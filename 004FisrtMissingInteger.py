# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.
def miss(arr,n):
    for i in range(n):
        if arr[i]<=0:
            arr[i]=n+1
    for i in range(n):
        index=abs(arr[i])
        if index>n:
            continue
        if arr[index-1]>0:
            arr[index-1]*=-1
    for i in range(n):
        if arr[i]>0:
            return i+1
    return n+1

arr=[int(x) for x in input("Enter array: ").split()]
print("First missing element in array is:",miss(arr,len(arr)))
