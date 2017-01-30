import time
import winsound

print('''
=================================================================
Description: A simple timer in minutes with beep alarm. PC Only.
Keywords [Python 3, Simple Timer, Minute Timer, Alarm, Winsound]
Jan 2017 v1.0
by
NoDisassemble.me
=================================================================
''')

while True:
    # user input for minutes
    minutes = input("Timer: How many minutes? ")
    # catch if not numbers
    if minutes.isdigit():
        pass
    else:
        print("")
        print("[!] Invalid entry. [!]")
        input("[!] Press Enter to try again:")
        print("")
        continue
    print("")
    # header
    print("[+] Starting timer: %0.f minutes. [+]" % int(minutes))
    print("")
    # loop for minutes passed
    count = 0
    while count < int(minutes):
        print("%0.i minutes passed. " % count)
        time.sleep(60)
        count += 1
    print("" + minutes + " minutes passed.")
    # footer
    print('''
     =======================
     [!] Timer complete. [!]
     =======================
    ''')
    # beep alert
    beepCount = 0
    while beepCount < 10:
        winsound.Beep(1000, 1000)
        time.sleep(1)
        beepCount += 1
    # restart timer
    input("Press Enter to restart timer.")
    print("")
