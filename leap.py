year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print("true")
elif year % 100 == 0:
    print("false")
elif year % 400 ==0:
    print("true")
else:
    print("false")
