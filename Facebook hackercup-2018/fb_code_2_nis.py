t=input()
for tc in range(t):
    n=input()
    p=[]
    #Get temp preceeding values (+)>(*)>(^)
    x=[0]*100
    for i in range(n+1):
        p.append(input())
    if n==0:
        print 'Case #'+str(tc+1)+': 0'
    elif n==1:
        print 'Case #'+str(tc+1)+': 1'
        print 0.0
    elif n>1:
        x[0]=1
        x[n]=p[n]
        # Calculation for P0 not required
        # ...P4*x^(4+P3*x^(3+P2*x^(2+p1)))
        for i in range(1,n):
            x[i]=i+1+p[i]
        for i in range(1,n):
            if x[i]==x[i-1]==0:
                x[i]=-1
        print 'Case #'+str(tc+1)+':',
        if x[n-1]==-1:
            print 1
            print 0.0
        else:
            print 0
        