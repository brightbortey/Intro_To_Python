#def personal_details():
#    name, age = "Simon", 19
#    address = "Bangalore, Karnataka, India"
#    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
#personal_details()
def get_age():
	age = int( input("What is your age?"))
	print("Age = ", age)
	return age

def get_name():
	name =  input("What is your name?")
	print("Name = ", name)
	return name

age = get_age()
name = get_name()

print (" ")
print ("Your Details")
print ("############")
print ("Name : ",name)
print ("Age : ",age)
