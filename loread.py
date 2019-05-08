#!/usr/bin/python3.6
import os
os.chdir("/var/log")
cmd="sudo cat auth.log | grep -i 'Accepted Publickey'"
std=os.system(cmd)

try: 
    day=input("Enter the day to which you want to see the logs from log file:")
except ValueError as e:
    print("Plz enter the valid date",e)
def dayCheckLog(day):
    with open("/home/shorab/basicpython/output.txt") as f:
        with open("log.txt","w") as f1:
            for line in f:
                words=line.split()
                for word in words:
                    if word==day:
                        f1.write(line)
dayCheckLog(day)
