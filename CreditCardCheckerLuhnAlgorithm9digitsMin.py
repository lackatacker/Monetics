a=input()
sum=0
i=len(a)-1
count=0
if(i<9):
    print('Too short to be valid!')
else:
    a=[int(x) for x in a]
    check=a[i]
    i-=1
    a=a[i::-1]
    while (count+1)<=i:
        u=a[count]*2
        if u>9:u=1+u%10
        sum+=u+a[count+1]
        count+=2
    if(count==i):
        u=a[i]*2
    if u>9:u=1+u%10
    sum+=u
    sum*=9
    if(sum%10==check):
        print("Valid Card!")
    else:
        print("Invalid Card!")
