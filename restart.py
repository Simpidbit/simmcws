import os
import time
from threading import Thread
import sys

pid = sys.argv[1]
time.sleep(1)
def main():
	os.system("python3 main.py")
Thread(target=main).start()

os.system("kill "+str(pid))
pid = os.getpid()
os.system("kill "+str(pid))
"""
		(OwO)
"""
