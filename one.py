#one.py

def fn():
	print ('function is in one.py')

print ('top level in one.py')

if __name__ == '__main__':
	print ('one.py is running directly')

else:
	print ('one.py is imported')

