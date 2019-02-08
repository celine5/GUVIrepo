x,y=input().split()
a = int(x)
b = int(y)
 
 
aaaa=""
 
for num in range(a,b):
 
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           aaaa = aaaa + str(num)+' ' 
 
print(aaaa.rstrip())
