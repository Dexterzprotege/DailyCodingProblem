# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def intervals(arr,n):
    j=0
    c=1
    i=1
    while i<n:
        if arr[i][0]>=arr[j][1]:
            c+=1
            j=i
        i+=1
    print(c)

l1=[int(x) for x in input("Enter starting intervals: ").split()]
l2=[int(x) for x in input("Enter ending intervals:").split()]
arr=[]
for i in range(len(l1)):
    temp=[]
    temp.append(l1[i])
    temp.append(l2[i])
    arr.append(temp)
arr.sort(key=lambda x: x[1])
intervals(arr,len(arr))