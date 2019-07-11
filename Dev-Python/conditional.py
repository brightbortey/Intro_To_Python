i = 8
if(i % 2 == 0): # % is modulo
    print ("Even Number")
else:
    print ("Odd Number")
    
def evens():
    list = []
    start = int(input("Enter Minimum Number"))
    finish = int(input("Enter Maximum Number"))
    for num in range(start,finish):#+1)
        if (num % 2 == 0):
            list.append(num)
    return list
print(evens())