import subprocess
import os
import fnmatch

# this is only OSX for now since that's where I'm hacking atm
ports_command = ["lsof", "-iTCP", "-sTCP:LISTEN", "-l", "-n", "-P"]
mem_command = ["vm_stat"]
disk_command = ["df"]

# get our open ports
ports_out = subprocess.check_output(ports_command)
print ports_out

# parse out the ports that are not on localhost

# get our current ram usage
mem_out = subprocess.check_output(mem_command)
print mem_out

# parse out the memory usage we need

# get the disk usage
disk_out = subprocess.check_output(disk_command)
print disk_out

# parse out the disk usage we need

pid_files = []

# troll for pid files for important processes
for root, _, files in os.walk("/var/run"):
    for pid in fnmatch.filter(files, "*.pid"):
        pid_files.append(os.path.join(root, pid))

print pid_files

process_status = {}

# check each one is running with kill 0

for pid_file in pid_files:
    pid = int(open(pid_file).read())
    running = True

    try:
        rv = os.kill(pid, 0)
    except OSError:
        running = False

    process_status[pid_file] = [pid, running]

print process_status

# connect to cctrl server
   # post our stats
   # get the current bots list and their ports

# next step is to use this list to do random checks of the other bots


