from functools import reduce

words = ['Hello','World']

def  join_strings(strings):
	return reduce(lambda x,y: x + ' ' + y,strings, 'Joy')
print(join_strings(words)) #joins the words together
