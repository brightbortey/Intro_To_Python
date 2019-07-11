print ("range 1")
for i in range(1,11):
	print (i)

print (" ")
print ("range 2")
for j in [1,2,3]:
	print (j)

print (" ")
print ("range 3")
for j in range(1,3):
	print (j)

print (" ")
type("1,2,3")

print (" ")
print ("using range to print list")
#a = [0,2,4,6,8,10,12,14,16,18]
for a in range(0,20):
	if a % 2 == 0:
		print (a)


print (" ")
print ("printing star 1 *")
def sparkle():
    b=1
    for b in range(1,5): #or while(b<5)
        print("****")           #print("****")
        b += 1                  #b = b + 1
sparkle()


print (" ")
print (" ")
print ("printing star 2*")
def star():
    i= 1
    for i in range (0,4):
        print("*")
        for j in range (0,i+4):
           print("*")
           i += 1<5
    print()
star()
      
print(" ")
print("true or false function 1(only a)")
def condition(): #function
    word = input("enter word")  #receive input of words
    found = False #boolean variable to check condition for specific letters
    for char in word: #for loop checks each character in the word
        if char == "a": #if statement to compare if word contains the letter a
            found = True #boolean variable set to true to confirm if a is found
    print(found) #print set outside funtion to print result only for one letter in word eg "a"in cat
condition()

print(" ")
print("true or false function 2(any other letter)")
def condition_2(letter):
    word = input("enter word")
    found = False
    for char in word:
        if char == letter:
            found = True
    print(found)

condition_2('y')
condition_2('z')
condition_2('a')

print(" ")
print("true or false function 3")
def condition_3(letter1,letter2): 
    word = input("enter word ")
    found = False #boolean variable
    for char in word:
        if char == letter1 or char == letter2:
            found = True
    print(found)

condition_3('s','m')

