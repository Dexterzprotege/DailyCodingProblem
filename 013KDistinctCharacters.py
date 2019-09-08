# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def kchars(s,k,n):
    ans = -1
    d = {}
    start = 0
    end = 0
    maxlen = 0
    st=""
    if k > n:
        print("-1")
    else:
        while end < n:
            key = s[end]
            if key not in d:
                d[key] = 1
            else:
                d[key] += 1
            while (len(d) > k):
                c = s[start]
                d[c] = d[c] - 1
                if (d[c] == 0):
                    del d[c]
                start = start + 1
            if maxlen<end-start+1:
                maxlen=end-start+1
                st=s[start:end+1]
            end = end + 1
        print("Max length=",maxlen)
        return (st)
s=str(input("Enter the string: "))
k=int(input("Enter window size: "))
print("Answer:",kchars(s,k,len(s)))