import paramiko
from config import *

# this will eventually be the basis of pushing the bot to a new machine
# and configuring it correctly.  I'm sure everyone will hate this part.

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

paramiko.util.log_to_file(log_file)
private_key = paramiko.RSAKey.from_private_key_file(rsa_private_key,
                                                    password=rsa_key_password)
ssh.connect(host_name, username=username, password='', pkey=private_key)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(status_command)

print ssh_stdout.read()
print ssh_stderr.read()

ssh_stdin.close()
