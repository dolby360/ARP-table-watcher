from ReadArp import ReadArpUtility
import subprocess
import time
import sys, getopt, os 


turnLog = False
def log(string,printThis = False):
        if turnLog or printThis:
                print(string)


receiverEmail="mrdolbyking@gmail.com" 
def sendEmail(attack_type,data):
	# add subject to mail text
	subject = "Subject: "+attack_type+" attack detected"
	command = "echo "+subject+" > email.txt"
	os.system(command)
	
	# add message to mail text
	os.system("echo ' ' >> email.txt")
	command = "echo " + data + " >> email.txt"
	os.system(command)
	# send mail text to receiver
	command="cat email.txt | sendmail "+receiverEmail
	os.system(command) 
	log("Report email sent!")

def deviceIP():
        bashCommand = "ifconfig wlan1 | grep inet | head -n 1 | awk '{ print $2 }'"        
        process = subprocess.check_output(bashCommand,shell=True)
        return str(process.decode("utf-8") )

def ping_all():
        while True: 
                log('Pinging everyones',True)    
                arpUtil = ReadArpUtility()
                #[:-1]  is for removing extra \n
                bashCommand = "fping -g " + deviceIP()[:-1] + '/24' + ' -q'
                log('Bash command:')
                log(bashCommand)
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.DEVNULL)
                output, error = process.communicate()
                log('output:')
                log(output)
                log('Error:')
                log(error)
                log('Pinging finished')
                time.sleep(20)