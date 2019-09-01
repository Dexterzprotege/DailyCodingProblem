# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
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
