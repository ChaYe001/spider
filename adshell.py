import subprocess

cmd = "adb shell 'cd sdcard/DCIM/LLVisionCamera && ls -l |wc -l'"

def adb_shell(cmd):
    p = subprocess.getstatusoutput(cmd)
    return p

result = adb_shell(cmd)
print(result[1])
