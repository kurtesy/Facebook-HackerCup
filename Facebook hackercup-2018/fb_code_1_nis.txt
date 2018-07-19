t=input()
for tc in range(t):
    n,k,v = map(int,raw_input().split())
    seen_tracker=[0]*n
    seen=(v-1)*k
    a=[]
    for i in range(n):
        a.append(raw_input())
    x=seen%n
    print 'Case #'+str(tc+1)+':',
    for i in range(0,k):
        ans=(x+i)%n
        seen_tracker[ans]=1
    for i in range(n):
        if seen_tracker[i]==1:
            print a[i],
    print