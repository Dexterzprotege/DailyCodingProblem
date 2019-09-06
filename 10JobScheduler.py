import time
def f():
    print("Scheduled!, where time is=",time.ctime())
def scheduler1(f,n):
    time.sleep(n/1000)
    f()
n=int(input("Enter time in milliseconds: "))
print("Current time=",time.ctime())
scheduler1(f,n)

