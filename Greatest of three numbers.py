n1=int(input("enter a number"))
n2=int(input())
n3=int(input())
if((n1>n2)&(n2<n1)):
    print("n1 largest")
elif((n2>n3)&(n2>n1)):
    print("n2 largest")
else:
    print("n3 largest")
