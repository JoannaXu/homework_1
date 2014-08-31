"""
	This part is a function definition, must be typed as 'def (name)():'
"""
def addition():
	"""
		This is a test of addition functions

		print will print out something to terminal so that you can see it

		str is a function which you can use to change numbers to strings

		a number is like 1,2,3,4

		a string is like "1, 2, 3" or like "this is good coffee"

		take the sentence "1 + 1" and add the sentence of the result of the math equation and then print it
		out to the terminal
	"""
	print("""
	
	This is the addition functions

		""")
	print("1 + 1 is = " + str((1 + 1)))
	print("3 + 3 is = " + str((3 + 3)))

def subtraction():
	"""
		This is some subtraction functions
	"""
	print("""
		This is the subtraction functions
	""")
	print("5 - 4 is = " + str(((5 - 4))))
	print("3 - 1 is = " + str(((3 - 1))))


"""
	We need this to tell the computer to run our program so we need to write some 
	code to tell it where to start, it starts after 

	if __name__ == '__main__':
		CODE
"""
if __name__ == '__main__':
	print("")
	print("This is my super awesome program")
	print("")
	addition()
	subtraction()