import subprocess, time

while True:
    try:
        subprocess.run("python main.py && python main2.py", shell=True)
    except:
        pass
    time.sleep(3)