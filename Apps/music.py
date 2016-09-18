import subprocess


def start():
    print "Starting music"
    # kill process if already running
    if is_started():
        stop()
    web_radio = "http://192.99.17.12:6410"
    command = "/usr/bin/mplayer %s " % web_radio
    print "execute command: %s" % command
    subprocess.Popen(command, shell=True)


def stop():
    print "Stopping music"
    p = subprocess.Popen("killall mplayer", shell=True)
    p.communicate()


def is_started():
    # check number of process
    p = subprocess.Popen("pgrep mplayer", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output == "":
        return False
    else:
        return True
