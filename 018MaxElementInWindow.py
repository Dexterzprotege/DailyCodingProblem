# This problem was asked by Google.
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# •	10 = max(10, 5, 2)
# •	7 = max(5, 2, 7)
# •	8 = max(2, 7, 8)
# •	8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
def slidingWindowMax(nums, k):
    j = k+1
    ans = []
    ans.append(max(nums[:k]))
    for i in range(len(nums)-k):
        new = nums[i+k]
        old = nums[i]
        if new>ans[-1]:
            ans.append(new)
        else:
            if ans[-1] == old:
                ans.append(max(nums[i+1:i+1+k]))
            else:
                ans.append(ans[-1])
    return ans
def maxinwind(arr,n,k):
    hs=dict()
    res=[]
    for i in range(k):
        if arr[i] not in hs:
            hs[arr[i]]=1
        else:
            hs[arr[i]]+=1
    res.append(max(hs))
    i=0
    j=k
    while j<n:
        c = arr[i]
        hs[c] = hs[c] - 1
        if (hs[c] == 0):
            del hs[c]
        if arr[j] not in hs:
            hs[arr[j]] = 1
        else:
            hs[arr[j]] += 1
        res.append(max(hs))
        i+=1
        j+=1
    return res

arr=[int(x) for x in input("Enter array elements: ").split()]
k=int(input("Enter window size: "))
print("Max ele are:",maxinwind(arr,len(arr),k))
