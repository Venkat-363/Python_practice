import math
n=int(input("Enter the First Number:"))
m=int(input("Enter the Second Number:"))

for i in range(n,m+1):
    d=0
    t=i
    arm=0
    while(i>0):
        i=i//10
        d+=1
    i=t
    while(t>0):
        r=t%10
        arm=arm+int(math.pow(r,d))
        t=t//10
    if(arm==i):
      print(arm,end=" ")
print()
        