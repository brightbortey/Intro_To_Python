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
		print (a, end = " , ")



def sparkle():
    b=1
    for b in range (0,5):
        #b = ("****")
        #print (b, end ="")
        print("****")
        b + = 1
sparkle()


print (" ")
print (" ")
print ("printing star *")
def star():
    #j= "*"
    for i in range (0,4):
        for j in range (0,i+4):
            print("*", end ="")
    print()
star()
        