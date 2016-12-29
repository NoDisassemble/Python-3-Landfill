import time

print('''
--------------------------------------------------------------------------
Description: A simple program that counts to whatever number you enter.
Keywords: [Python 3, Count To A Number, Python Counting]
Dec 2016 v1.0
by
NoDisassemble.me
--------------------------------------------------------------------------
''')

while True:
    try:
        count=1
        x=int(input("Enter a number to count to: "))
        print("[+] Counting to " + str(x) + " [+]")
        time.sleep(1)
        while count<x+1:
            print (count)
            count=count+1
        print("[!] Count Completed [!]")
        print("")
        input("Press Enter to run again:")
        print("")
    except ValueError:
        print("")
        print("Invalid response:")
        input("Press enter to try again:")
        print("")
