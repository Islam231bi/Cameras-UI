import os
import signal
import subprocess
import time

p = subprocess.Popen(["python3", "cam.py"])
time.sleep(10)
os.kill(p.pid, signal.SIGTERM)
print(p.pid)