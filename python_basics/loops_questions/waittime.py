import time

waittime = 1
attempts = 0

while attempts < 5:
    print("Attempts", attempts + 1, "waiting time ", waittime)
    time.sleep(waittime)
 # time.sleep makes the system stop working for the given peroid of time 
    waittime = waittime * 2 
    attempts = attempts + 1