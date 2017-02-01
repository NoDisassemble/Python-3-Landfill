import time

print('''
-----------------------------------------------------------------------------
Description: A simple program that counts to whatever whole number you enter.
Keywords [Count To A Number, Python Counting]
Jan 2017 v2.0
by
NoDisassemble.me
-----------------------------------------------------------------------------
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
