"""
take smal piece of titanic data which can get from kaggle.com
take the passenger id from the user and give information of name
and survieved or not
Algorithm:
	take the data from file
	Store it in a dictionary
	get the passengerid from the user
	make a lookup from the defined dictionary to check the details
	if find:
		return details
	else:
		return "passenger id not found" 
""" 

# importing user defind module file_operations
import file_operations as fo
# calling get_data function from module file_operations
data=fo.get_data()
# data is the list of all lines i.e data is a list, one line in file is one element in the list 
# uncomment below line to check the data 
#print data
# data list contains first element as column names
# get the first element of the data using zero index
columns=data[0]
columns=columns.split(',')
# uncomment the below line to check columns output
#print columns
# second element in columns list contains extra "\n"
# below statement remoes that
columns_req=[] # empty list to store columns
for i in columns:
	"""
		looping through the columns to remove new line character
	"""
	i=i.strip("\n") # strip function strip the characters specified in the arguments list
	columns_req.append(i)
# uncomment below line to check columns
#print columns_req
data_list=[] # empty list for data
for i in data[1:]:
	d=i.split(',')
	data_list.append({'passengerid':d[0],
							'Survived':d[1],
							'Name':" ".join(d[2:])
		})
# uncomment below line to check the list of dictionaries
#print data_list[0]
def get_info(pid):
	result=""
	for i in data_list:
		if i.get('passengerid',False)==pid:
			survieved=i.get('Survived')
			if survieved=='0':
				result=result+"Survived: No"
			else:
				result=result+"Survived: Yes"
			result=result+" "+"Name: "+i.get('Name')
			return result
	return False
while True:
	pid=raw_input("Enter passenger id or 'q' to quit the program:")
	if pid=='q':
		break
	else:
		information=get_info(pid)
		if information:
			print information
		else:
			print "passenger id not found"




