n=int(input("Enter the Number:"))
h=n%10
while n!=0:
    r=n%10
    n=n//10
    if(r>h):
        h=r
print(h)