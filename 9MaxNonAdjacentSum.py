def maxsum(arr,n):
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2],arr[i],arr[i]+dp[i-2])
    return dp[n-1]
def maxsum2(arr,n):
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