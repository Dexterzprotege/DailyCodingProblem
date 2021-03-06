# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

def decode(arr,n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1 if arr[0]!='0' else 0
    for i in range(2,n+1):
        if arr[i-2]!='0' and int(arr[i-2:i])<27:
            dp[i]+=dp[i-2]
        if arr[i-1]!='0':
            dp[i]+=dp[i-1]
    return dp[-1]


st=str(input())
print(decode(st,len(st)))
