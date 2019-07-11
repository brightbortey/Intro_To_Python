print (" ")
print ("printing only even numbers")
first =  int ( input("enter first number"))
last = int ( input("enter last number"))
for num in range(first,last+1):
        if num % 2 == 0:
                print (num)

