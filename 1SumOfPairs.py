def func(arr,k):
    arr.sort()
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]+arr[j]==k:
            return True
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1
    return False
arr=[int(x) for x in input("Enter array: ").split()]
k=int(input("Enter K: "))
print(func(arr,k))
