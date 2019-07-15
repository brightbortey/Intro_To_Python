def is_even(x):

	return x % 2 == 0

print(is_even(3))
print(is_even(4))


print(" ")
def is_evens():   #function name
	numbers = [1,56,234,87,4,76,24,69,90,135]  #list of numbers
	found = False  #boolean
	evens = []    #empty list to store even numbers
	for i in numbers:   #check all numbers to find numbers when divided by 2 = o
		if i %2  == 0: #if numbers when divided by 2=o
			found = True  #boolean is true
			evens.append(i) #add all even numbers to the list

	print (list(evens))
is_evens()






#using lambda
print (" ")
print("even ")
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(lambda x: x %2 == 0,numbers)))


#odd numbers
#using lambda
print(" ")
print ("Odd Numbers ")
print(list(map(lambda x: x %2 == 1,numbers)))
print(list(filter(lambda x: x %2 == 1,numbers)))   #for x %2 ==1,all divided by 2 with remainder 1 is odd

#map true or false
#filter checks through all the elements in the list
