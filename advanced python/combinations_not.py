#the function 'not' combines two situations for eg x=true.....if we check the 
#variable in x and it is 'not true', then it is false

def is_odd(x):
	if not x % 2 == 0:
		return False
	else:
		return True

print(is_odd(5))





print (" ")
def is_evens():   #function name
	numbers = [1,56,234,87,4,76,24,69,90,135]  #list of numbers
	evens = []    #empty list to store even numbers
	for i in numbers:   #check all numbers to find numbers when divided by $
		if not i %2  == 0: #if numbers when divided by 2=o
			#return False
			if i%2 == 1:
				#return True #boolean is true
				evens.append(i) #add all even numbers to the list

	print (list(evens))
print(is_evens())

