import time
import sys
import multiprocessing
import uuid

print('''
-----------------------------------------------------------------------------------
A simple multiprocessing program that runs 2 loading bars and displays their UID.
Keywords [Multiprocessing, UUID, Loading Bar]
Dec 2016 v1.0
by
Nodisassemble.me
-----------------------------------------------------------------------------------
''')

# Program for Loading Bar 1
def loadingBar1():
    loading = "[+] Loading Bar 1: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    # Prints UID
    print("[+] Unique Id: {0}".format(uuid.uuid1()))
    print("[!] Finished")

# Program for Loading Bar 2
def loadingBar2():
    print("")
    loading = "[+] Loading Bar 2: [-------------------]"
    for i in range(101):
        time.sleep(0.03)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    # Prints UID
    print("[+] Unique Id: {0}".format(uuid.uuid1()))
    print("[!] Finished")
    print("")

while True:
    # Run main program
    if __name__ == '__main__':
        process1 = multiprocessing.Process(target=loadingBar1())
        process2 = multiprocessing.Process(target=loadingBar2())
        # Start processes
        process1.start()
        process2.start()

        process1.terminate()
        process2.terminate()
    input("Press Enter to run again:")
    print("")
