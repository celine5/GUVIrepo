m,n=input().split()
a = int(m)
c = int(n)
 
 
aaaa=""
 
for num in range(a,c):
 
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           aaaa = aaaa + str(num)+' ' 
 
print(aaaa.rstrip())
