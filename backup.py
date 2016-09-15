import paramiko as pmk
ssh = pmk.SSHClient()
from threading import Thread
import time
import os
buffer_time_file = '/home/nexii/.buffer_time'
pmk.util.log_to_file("filename.log")
def data_reset(ssh):
	print "Recovery started.."
	cmd1 = "rsync -avz backup/source/* recovery"
	in1,out,err = ssh.exec_command(cmd1)
	d=out.readlines()
	cmd2 = "rsync -avz buffer/* recovery"
	in1,out,err = ssh.exec_command(cmd2)
	d=out.readlines()
	
def makeit_buffer(count):
	print "data buffer operation started"
	while True:
			if count == 50:
				break
			f=open("/home/nexii/buffer/f{0}.txt".format(count),'w')
			for i in range(100):
				f.write(str(i)+"->")
				if i%5==0:
					f.write("\n")
				f.flush()
			count+=1
			f.close()
			time.sleep(1)
	
def data_read(file_name):
	r1_source = '/home/nexii/source/'+file_name
	r1_backup = '/home/nexii/backup/source/'+file_name
	r1_buffer = '/home/nexii/buffer/'+file_name
	f=False
	if os.path.isfile(r1_source):
		print "reading {0} from source".format(file_name)
		f=open(r1_source)
	elif os.path.isfile(r1_backup):
		print "reading {0} from backup".format(file_name)
		f=open(r1_backup)
	elif os.path.isfile(r1_buffer):
		print "reading {0} from buffer".format(file_name)
		f=open(r1_buffer)
	else:
		print "file {0} Not found".format(file_name)
	if f:
		print f.read()
		f.close()


def data_write(ssh,source,destination):
	print "data write operation started"
	count = 0
	while True:
		try:
			f=open("/home/nexii/source/f{0}.txt".format(count),'w')
			for i in range(100):
				f.write(str(i)+"->")
				if i%5==0:
					f.write("\n")
				f.flush()
				# backup code
				cmd = "rsync -aE --delete --progress {0} {1}".format(source,destination)
				stdin,stdout,stderr = ssh.exec_command(cmd)
				out=stdout.readlines()
			f.close()
			count+=1
		except Exception as err:
			print "===============================>>>>>",err
			print "write in to souce folder stopped"
			makeit_buffer(count)
			break

ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
host = "localhost"#raw_input("Enter host:")
username = "nexii"#raw_input("Enter username:")
pwd= "nexii"#raw_input("Enter password:")
sudo_pwd = "nexii" #raw_input("Enter sudo password:")
sudo = "echo "+sudo_pwd+"| sudo -S "
source = "/home/nexii/source" # raw_input("Enter Source folder name: ")
destination = "/home/nexii/backup"#raw_input("Enter destination folder name: ")
buffer_folder = "buffer"# raw_input("Enter Buffer folder name:")
ssh.connect(host,username=username,password=pwd)
t1 = Thread(target=data_write,args=(ssh,source,destination))
t1.start()
print "writing and backingup..............."
time.sleep(2)
print "read operation for f0.txt"
data_read("f0.txt")
time.sleep(10)
print "removing source file........."
in1,out,err=ssh.exec_command("rm -r source")
out1=out.readlines()
print "--------------> Source file deleted .........."
print "read operation for f0.txt"
data_read("f0.txt")
time.sleep(5)
print "read operation for f11.txt"
data_read("f11.txt")
time.sleep(2)
print "read operation for f100.txt"
data_read("f100.txt")
data_reset(ssh)
time.sleep(10)
data_reset(ssh)





