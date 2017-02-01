import sys
import time

print('''
===================================================================================
 _______               ___.                     _____                 .__
 \      \  __ __  _____\_ |__   ___________    /     \ _____     ____ |__| ____
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \  /  \ /  \\\__  \   / ___\|  |/ ___\\
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ /    Y    \/ __ \_/ /_/  >  \  \___
\____|__  /____/|__|_|  /___  /\___  >__|    \____|__  (____  /\___  /|__|\___  >
        \/            \/    \/     \/                \/     \//_____/         \/
===================================================================================

Description: Simple number magic trick.
Keywords: [Python 3, Number Magic Trick]
Feb 2017 v1.0
by
NoDisassemble.me
-----------------------------------------------------------------------------------
''')

while True:
    name = input("Your name? ")
    print("")
    print("Hello " + name + ". My name is Prime, wizard of all that is numbers.")
    trick = str(input("Would you like to see a magic trick? [Yes or No]: "))
    if trick in ["Yes", "yes", "Y", "y"]:
        print("Oh great! This is a wonderful magic trick. You will learn the answer to the "
              "ultimate question of Life, the Universe, and Everything in it.")
    else:
        print("Well '%s' wasn't really the response I was looking for, but I am going to "
              "show you my trick anyway." % trick)
    time.sleep(7)
    print("We are going to do some simple math, and I will guess the number you are left with.")
    time.sleep(3)
    print("Lets begin!")
    time.sleep(2)
    print("Think of a number between 1 and 100.")
    print("Enter it into your calculator.")
    input("Press Enter to continue...")
    print("[+] Add 1042 to your number.")
    input("Press Enter to continue...")
    print("[+] Now Add 775 to your number.")
    input("Press Enter to continue...")
    print("[-] Subtract 462 from your number.")
    input("Press Enter to continue...")
    print("[-] Now Subtract 1024 from your number.")
    input("Press Enter to continue...")
    print("[+] Add 995 to your number.")
    input("Press Enter to continue...")
    print("[+] Now Add 563 to your number.")
    input("Press Enter to continue...")
    print("[-] Subtract 1847 from your number.")
    input("Press Enter to continue...")
    print("[-] And finally, Subtract your original number you thought of...")
    input("Press Enter to continue...")
    print("")
    loading = "Calculating all possible answers including infinity: [-------------------]"
    for i in range(101):
        time.sleep(0.1)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 \
                or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 \
                or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
            # sys.stdout.flush()
    print("")
    time.sleep(3)
    print("")
    print("Thinking...")
    time.sleep(3)
    print("")
    print("Thinking some more...")
    time.sleep(3)
    print('')
    print("Still thinking...")
    time.sleep(3)
    print("")
    print("Hey this isn't easy you know.  Just because I am all knowing and a number wizard "
          "doesn't mean I can guess your number correctly.")
    time.sleep(5)
    print("")
    print("Just kidding " + name + ". The number you are left with is 42. =)")
    print("")
    input("Press Enter to see my trick again.")
    print("")
