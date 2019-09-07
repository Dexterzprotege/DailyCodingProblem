# This problem was asked by Amazon.
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# •	1, 1, 1, 1
# •	2, 1, 1
# •	1, 2, 1
# •	1, 1, 2
# •	2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

def stairs(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
def stairs2rec(arr,n):
    if n==0:
        return 1
    total=0
    for i in arr:
        if n-i>=0:
            total+=stairs2rec(arr,n-i)
    return total
def stairs2(arr,n):
    if n==0:
        return 1
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,n+1):
        total=0
        for j in arr:
            if i-j>0:
                total+=dp[i-j]
        dp[i]=total
        dp[i]+=1 if i in arr else 0
    return dp[-1]

n=int(input("Enter number of steps(1,2 hops): "))
print("No.of ways to climb:",stairs(n))
arr=[int(x) for x in input("Enter the hops: ").split()]
m=int(input("Enter number of steps(X hops): "))
print("No.of ways to climb:",stairs2rec(arr,m))
print("No.of ways to climb (Optimized) :",stairs2(arr,m))
