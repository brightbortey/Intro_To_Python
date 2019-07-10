#to view line numbers use nano -c person.py

i = 0
while(i < 10):
	i = i + 1
	print (i)

print (" ")
print ("For numbers From 7 to 19")
i = 6
while(i < 19):
	i = i + 1
	print (i)

print (" ")
print ("For even numbers between 12 and 20")
i = 12
while(i < 18):
	i = i + 2
	print (i)

def evens():

	print (" ")
	print ("printing only even numbers")
	first =  int ( input("enter first number"))
	last = int ( input("enter last number"))
	for num in range(first,last+1):
		if num % 2 == 0:
			print (num, end = " ")
evens()



def reverse_evens():
	print (" ")
	print ("printing only even numbers")
	first =  int ( input("enter first number"))
	last = int ( input("enter last number"))
	for num in range(first,last+1):
		if num % 2 == 0:
			num.reverse()
			print (num, end = " ")
reverse_evens()

