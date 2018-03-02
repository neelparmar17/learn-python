import subprocess
import os
import stat

os.chmod("demoscript.sh", 0o777)
print("start")
subprocess.call("./demoscript.sh", shell=True)
print("end")
