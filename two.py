#two.py

import one

print ('top level in two.py')

one.fn()

if __name__ == '__main__':
	print ('two.py is running directly')

else:
	print ('two.py is imported')