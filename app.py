import subprocess
pingUrl = "www.fsf.org"
def getPingTime(pingUrl):
    # Ping time in miliseconds
    pingTime = subprocess.check_output(["ping", pingUrl, "-c", "1"])
    pingTime = str(pingTime)
    pingTime = pingTime.split("time=")
    pingTime = pingTime[1].split("\\n")
    pingTime = pingTime[0][0:-3]
    pingTime = float(pingTime)
    print(str(pingTime))
