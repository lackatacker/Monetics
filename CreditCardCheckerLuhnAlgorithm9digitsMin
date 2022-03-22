a=input()
sum=0
i=len(a)
count=0
if(i<9):
    print('Too short to be valid!')
else:
    for k in a:
        k=int(k)
    check=int(a[i-1])
    i-=2
    a=a[i::-1]
    while (count+1)<=i:
        u=int(a[count])*2
        if u>9:u=1+u%10
        new=u+int(a[count+1])
        sum+=u+int(a[count+1])
        count+=2
    if(count==i):
        u=int(a[i])*2
    if u>9:u=1+u%10
    sum+=u
    sum*=9
    if(sum%10==check):
        print("Valid Card!")
    else:
        print("Invalid Card!")

