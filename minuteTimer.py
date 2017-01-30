import time

print('''
=================================================
Description: A simple timer in minutes.
Keywords [Python 3, Simple Timer, Minute timer.]
Jan 2017 v1.0
by
NoDisassemble.me
=================================================
''')

while True:
    minutes = input("Timer: How many minutes? ")
    if minutes.isdigit():
        pass
    else:
        print("")
        print("[!] Invalid entry. [!]")
        input("[!] Press Enter to try again:")
        print("")
        continue
    print("")
    print("[+] Starting timer: %0.f minutes. [+]" % int(minutes))
    print("")
    count = 0
    while count < int(minutes):
        print("%0.i minutes passed. " % count)
        time.sleep(60)
        count += 1
    print("" + minutes + " minutes passed.")
    print('''
     =======================
     [!] Timer complete. [!]
     =======================
    ''')
    input("Press Enter to restart timer.")
    print("")
