1.sum = 0
list = [11,22,33,44,55,66,77]
for num in list:
    sum = sum +num
average  = sum / len(list)
print ("sum of list element is : ", sum)
print ("Average of list element is ", average )
---------------------------------------------------------------------------------------------------------    
2.lst = []
num = int(input('How many numbers: '))
 
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
 
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
