# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def mul(arr,n):
    l=[0]*n
    r=[0]*n
    l[0]=1
    r[n-1]=1
    for i in range(1,n):
        l[i]=l[i-1]*arr[i-1]
    for i in range(n-2,-1,-1):
        r[i]=r[i+1]*arr[i+1]
    res=[0]*n
    for i in range(n):
        res[i]=l[i]*r[i]
    return res

arr=[int(x) for x in input("Enter array: ").split()]
print(mul(arr,len(arr)))
