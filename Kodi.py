import subprocess


class Kodi:
    """
    Constructor
    """

    def __init__(self):
        self.status = self.is_started()

    def is_started(self):
        # check number of process
        p = subprocess.Popen("pgrep /usr/bin/kodi", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output == "":
            return False
        else:
            return True

    def play(self):
        # kill process if already running
        if not self.is_started():
            command = " export DISPLAY=:0.0; /usr/bin/kodi %s"
            print "execute command: %s" % command
            p = subprocess.Popen(command, shell=True)

    def stop(self):
        p = subprocess.Popen("ps -ef | grep kodi | grep -v grep | awk '{print $2}' | xargs kill -9", shell=True)
        (output, err) = p.communicate()
