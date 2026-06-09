#fabonacci system for pro1
def fabo(num):
    prev=0
    next=1
    i=0
    if i==num:
        fabonacci=prev
    else:
        if num==1:
            fabonacci=next
        else:
            i=2
            while i<=num:
             temp=prev+next
             prev=next
             next=temp
             i=i+1
             fabonacci=temp
    return fabonacci
a=int(input('Enter number   '))
print('Fabonacci',a,'is',fabo(a))