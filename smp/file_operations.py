"""
 Conditional statements(if..then)
Looping
User-defined functions
Use of modules(creating and importing)
Reading/writing files
Exception handling
Lists and/or Dictionaries
Prompting user for input 
Validating input(using while loops)
Displaying output to the screen.
"""
# importing os module to work with os kind of operations
import os
def get_data():
	"""
	returns the data from a file 
	"""
	try:
		path=os.path.join('data','data.csv')
		f=open(path)
		data=f.readlines()
		return data
	except Exception as err:
		return err

