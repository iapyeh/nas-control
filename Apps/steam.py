import subprocess


def start():
    print "Starting Steam"
    # kill process if already running
    if not is_started():
        command = "export DISPLAY=:0.0; /usr/games/steam -bigpicture"
        print "execute command: %s" % command
        subprocess.Popen(command, shell=True)


def stop():
    print "Stopping Steam"
    p = subprocess.Popen("ps -ef | grep steam | grep -v grep | awk '{print $2}' | xargs kill -9", shell=True)
    p.communicate()


def is_started():
    # check number of process
    p = subprocess.Popen("pgrep /usr/bin/steam", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output == "":
        return False
    else:
        return True
