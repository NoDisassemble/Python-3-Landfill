import time

print('''
--------------------------------------------------------------------------
A simple program that counts to whatever number you enter.
Keywords [Count To A Number, Python Counting]
Dec 2016 v2.0
by
NoDisassemble.me
--------------------------------------------------------------------------
''')

while True:
    try:
        number = int(input("Enter whole number to count to: "))
    except ValueError:
        print("")
        print("[!] Invalid entry. Must be a whole number. [!]")
        input("Press Enter to try again")
        print("")
        continue
    print("")
    print("[+] Counting to", number, "[+]")
    count = 1
    while count <= int(number):
        time.sleep(.3)
        print(count)
        count += 1
    print("[!] Counting complete [!]")
    print("")
    input("Press enter to count again.")
    print("")
