t=input()
for tc in range(t):
    a=raw_input()
    nhi_hoga = True
    i,k=1,0
    ans=a
    occurance = [0]* len(a)
    while i<len(a):
        if a[i]!=a[k]:
            if k==0:
                occurance[i] = 0
                i+=1
            else:
                k = occurance[k-1]
        else:
            k+=1
            occurance[i] = k
            i+=1
    for i in range(len(a)):
        if occurance[i]:
            if occurance[i]*2 < i+1 and occurance[i+1] <= occurance[i]:
                nhi_hoga=False
                ans=ans[:i]+ans
                break
    if nhi_hoga:
        print 'Case #'+str(tc+1)+': Impossible'
    else:
        print 'Case #'+str(tc+1)+': '+ans