import subprocess


def start():
    print "Starting Kodi"
    # kill process if already running
    if not is_started():
        command = " export DISPLAY=:0.0; /usr/bin/kodi"
        print "execute command: %s" % command
        subprocess.Popen(command, shell=True)


def stop():
    print "Stopping Kodi"
    p = subprocess.Popen("ps -ef | grep kodi | grep -v grep | awk '{print $2}' | xargs kill -9", shell=True)
    p.communicate()


def is_started():
    # check number of process
    p = subprocess.Popen("pgrep /usr/bin/kodi", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output == "":
        return False
    else:
        return True
