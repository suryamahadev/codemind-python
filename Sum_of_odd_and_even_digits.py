x=int(input())
sum=0
sum1=0
a=list(map(int,input().split()))
for i in range(0,x):
    if i%2==0:
        sum=sum+a[i]
    else:
        sum1=sum1+a[i]
if sum-sum1==0:
    print('YES')
else:
    print('NO') 
