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