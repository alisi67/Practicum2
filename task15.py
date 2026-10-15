n,k,m=map(int,input().split())
if (n-k)<=m:
    print(n-k+m-1)
else:
    print(m-k-1)