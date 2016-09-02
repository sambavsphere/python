import paramiko as pmk
import re
ssh = pmk.SSHClient()
ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
ssh.connect("192.168.5.64",username="",password="")
ssh.exec_command("mkdir mydear")
sftp = ssh.open_sftp()
sftp.put("local.py","./mydear/local.py")
ssh.exec_command("python ./mydear/local.py")
stdin,stdout,stderr=ssh.exec_command("ls -l")
print ssh.exec_command("ls -l")
print stdout.readlines()


pwd = "echo pwd| sudo -S"
stdin,stdout,stderr = ssh.exec_command("echo pwd| sudo -S ls /proc")
data = stdout.read()
ls_folders=re.findall(".+[a-z]$",data,re.M)
f = open("System information.txt",'w')
try:
	for folder in ls_folders:
		message="""
				..................................................................
									{0}:Information
				..................................................................
				""".format(folder)
		stdin,stdout,stderr  = ssh.exec_command("{0} cat /proc/{1}".format(pwd,folder))
		f.write(message+"\n")
		f.writelines(stdout.readlines())
		print "written {0} folder info".format(folder)
except Exception as err:
	print err
finally:
	f.close()


ssh.close()
