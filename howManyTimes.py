import time

print('''
--------------------------------------------------------------------------------
Description: A simple program that prints whatever you type for however many times you say.
Keywords: [Python Word Repeater, Character Repeater]
Dec 2016 v1.0
by
NoDisassemble.me
--------------------------------------------------------------------------------
''')

while True:
    what=input("What would you like to say? ")
    try:
        x=int(input("How many times to say it? "))
        print("")
        print("[+] Typing " + str(what) + " " + str(x) + " times [+]")
        time.sleep(1)
        while x != 0:
            print(what)
            x = x - 1
        print("[!] Typing Completed [!]")
        print("")
        input("Press Enter to run again:")
        print("")
    except ValueError:
        print("")
        print("Invalid response:")
        input("Press Enter to try again:")
        print('')
        continue
