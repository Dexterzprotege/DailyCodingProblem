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
    return n+1;
arr=[int(x) for x in input("Enter array: ").split()]
print("First missing element in array is:",miss(arr,len(arr)))