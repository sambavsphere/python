'''
Input:
Program takes host, username,password, sudo password and  the config file that contains three columns. 1.command(command to execute in given vm ex: ls -l) 
2. sudo(Does this command required sudo permission(1/0 or True/False))
3. Value( result of the command)

Output:
	Program adds the new column called "result" to the existing config file, stores 1/0 based on the value.
'''


import paramiko as pmk
ssh = pmk.SSHClient()
import sys
import os
import pandas as pd
ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
host = raw_input("Enter host:")
username = raw_input("Enter username:")
pwd= raw_input("Enter password:")
sudo_pwd = raw_input("Enter sudo password:")
sudo = "echo "+sudo_pwd+"| sudo -S "

def get_cmd_data(cmd):
	'''
	function returns an error message if the command gives any error message
	otherwise returns the command output
	This function has some problems, it's still need some improvement
	'''
	stdin,stdout,stderr = ssh.exec_command(cmd)
	error = stderr.read()
	if error.find('password for ') != -1:
		return stdout.read()
	elif error:
		return error
	else:
		return stdout.read()


while True:
	config_file_path = raw_input("Enter Config File Path:")
	if not os.path.isfile(config_file_path):
		option = raw_input("file is not there:\n\t Enter y to enter new file path \n\t Enter n to exit")
		if option == 'n':
			sys.exit(0)
		elif option == 'y':
			continue
		else:
			print "wrong option!!!!!!!!!!"
	else:
		file_data = pd.read_csv(config_file_path)
		break
try:
	ssh.connect(host,username=username,password=pwd)
	res=[]
	for row in file_data.index:
		command = file_data.ix[row]['command']
		root = file_data.ix[row]['sudo']
		value = file_data.ix[row]['value']
		if root:
			command = sudo+command
		res.append(1) if value == get_cmd_data(command) else res.append(0)  
	file_data['result'] = res
	file_data.to_csv(config_file_path)
except Exception as err:
	print err



