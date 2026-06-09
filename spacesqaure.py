n=int(input("enter the number of rows"))
k=n-1
j=1
for i in range(n):
    print(" "*k,"* "*j)
    j+=1
    k-=1