#Problem Link: https://www.codechef.com/COOK106B/problems/REACTION

t = int(input())
while t:
    t-=1
    r,c = map(int, input().split())
    a = [0]*r
    f = 0
    for x in range(r):
        a[x] = list(map(int, input().split()))
    for i in range(r):
        for j in range(c):
            if i-1>=0:
                f+=1
            if i+1<r:
                f+=1
            if j-1>=0:
                f+=1
            if j+1<c:
                f+=1
            if f>a[i][j]:
                k=1
            else:
                k=0
                break
            f=0
        if k==0:
            break
    if k==0:
        print("Unstable")
    else:
        print("Stable")
            
