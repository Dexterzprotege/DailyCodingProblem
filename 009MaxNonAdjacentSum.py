# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

def maxsum(arr,n):  #Complexity O(N), O(N)
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2],arr[i],arr[i]+dp[i-2])
    return dp[n-1]
def maxsum2(arr,n):  #Complexity O(N), O(1)
    sum= max(arr[0],arr[1])
    maxOne = sum
    maxTwo= arr[0]
    for i in range(2,n):
        sum=max(maxOne,maxTwo+arr[i])
        maxTwo=maxOne
        maxOne=sum
    return sum
arr=[int(x) for x in input("ENTER ARRAY: ").split()]
print("The max non adjacent subarray sum is:",maxsum(arr,len(arr)))
print("The max non adjacent subarray sum(Optimized) is:",maxsum2(arr,len(arr)))
