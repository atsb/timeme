#!/usr/bin/python
help = """Usage: timeme [OPTION]... [OPTION]...
Counts down to zero from the desired time.
Useful in timing yourself during tasks or extreme programming.

Mandatory arguments.
timer, 10 - 60.			This starts the timer from the chosen time.
"""
import sys, time
def start60():
    timer = 3600.00
    alert = time.time() + timer
    while True:
        ticktock = time.time()
        if ticktock < alert:
            time.sleep(1.0)
            print('Time Remaining(seconds): {}\r'.format(round(alert - ticktock))),
        else:
            print("\n60 Minutes is up!")
            break
def start50():
    timer = 3000.00
    alert = time.time() + timer
    while True:
        ticktock = time.time()
        if ticktock < alert:
            time.sleep(1.0)
            print('Time Remaining(seconds): {}\r'.format(round(alert - ticktock))),
        else:
            print("\n50 Minutes is up!")
            break
def start40():
    timer = 2400.00
    alert = time.time() + timer
    while True:
        ticktock = time.time()
        if ticktock < alert:
            time.sleep(1.0)
            print('Time Remaining(seconds): {}\r'.format(round(alert - ticktock))),
        else:
            print("\n40 Minutes is up!")
            break
def start30():
    timer = 1800.00
    alert = time.time() + timer
    while True:
        ticktock = time.time()
        if ticktock < alert:
            time.sleep(1.0)
            print('Time Remaining(seconds): {}\r'.format(round(alert - ticktock))),
        else:
            print("\n30 Minutes is up!")
            break
def start20():
    timer = 1200.00
    alert = time.time() + timer
    while True:
        ticktock = time.time()
        if ticktock < alert:
            time.sleep(1.0)
            print('Time Remaining(seconds): {}\r'.format(round(alert - ticktock))),
        else:
            print("\n20 Minutes is up!")
            break
def start10():
    timer = 600.00
    alert = time.time() + timer
    while True:
        ticktock = time.time()
        if ticktock < alert:
            time.sleep(1.0)
            print('Time Remaining(seconds): {}\r'.format(round(alert - ticktock))),
        else:
            print("\n10 Minutes is up!")
            break
if(len(sys.argv)<3):
    print(help)
elif(len(sys.argv)>3):
    print("Invalid number of arguments")
elif(sys.argv[1] == 'timer') & (sys.argv[2] == '60'):
	print("Starting 60 Minute Countdown...")
	start60()
elif(sys.argv[1] == 'timer') & (sys.argv[2] == '50'):
	print("Starting 50 Minute Countdown...")
	start50()
elif(sys.argv[1] == 'timer') & (sys.argv[2] == '40'):
	print("Starting 40 Minute Countdown...")
	start40()
elif(sys.argv[1] == 'timer') & (sys.argv[2] == '30'):
	print("Starting 30 Minute Countdown...")
	start30()
elif(sys.argv[1] == 'timer') & (sys.argv[2] == '20'):
	print("Starting 20 Minute Countdown...")
	start20()
elif(sys.argv[1] == 'timer') & (sys.argv[2] == '10'):
	print("Starting 10 Minute Countdown...")
	start10()
else:
	print("Unrecognized Option.")
