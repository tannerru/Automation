#Network Device Backup

 # import modules needed and set up ssh connection parameters
import paramiko
import datetime
import time
user = 'username'
secret = 'password'
port = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
# define variables
time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
infilepath = "rootpath"
devicelist = "device-list.txt"
 
# open device file
input_file = open( infilepath + devicelist, "r")
iplist = input_file.readlines()
input_file.close()
 
# loop through device list and execute commands
for ip in iplist:
    ipaddr = ip.strip()
    ssh.connect(hostname=ipaddr, username=user, password=secret, port=port)
    client=ssh.invoke_shell()
    time.sleep(2)
    output=client.recv(65535)

    client.send(f"copy running-config tftp://IPADDRESS/runningconfig-{ipaddr}-{time_now}.cfg\n")
    time.sleep(2)
    output=client.recv(65535)
ssh.close()
    
 
  
  
    