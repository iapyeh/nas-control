import subprocess


class Player:
    """
    Constructor
    """
    def __init__(self):
        self.status = self.isStarted()
        
    def is_started(self):
        # check number of process
        p = subprocess.Popen("pgrep mplayer", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output =="":
                return False
        else:
                return True
            
    def play(self, radio):
        # kill process if already running
        if self.is_started():
            self.stop()
        command = "/usr/bin/mplayer %s" % radio
        print "execute command: %s" % command
        p = subprocess.Popen(command, shell=True)

    def stop(self):
        p = subprocess.Popen("killall mplayer", shell=True)
        (output, err) = p.communicate()
