from ReadArp import ReadArpUtility
import subprocess
import time

turnLog = False
def log(string,printThis = False):
        if turnLog or printThis:
                print(string)


def ping_all():
        while True: 
                log('Pinging everyones',True)    
                arpUtil = ReadArpUtility()
                bashCommand = "fping -g " + arpUtil.get_pairs_of_mac_and_ip()[0][1] + '/24' + ' -q'
                log('Bash command:')
                log(bashCommand)
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.DEVNULL)
                output, error = process.communicate()
                log('output:')
                log(output)
                log('Error:')
                log(error)
                log('Pinging finished',True)
                time.sleep(20)