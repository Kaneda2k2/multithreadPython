#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hochi
#
# Created:     05/09/2021
# Copyright:   (c) hochi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##### ABRIR PROGRAMAS EXTERNOS CON PYTHON

###subprocess.Popen
##import subprocess
##
##print(subprocess.Popen('C:\\Windows\\System32\\calc.exe'))


##############################################
###################ABRIENDO PROGRAMAS
##import subprocess
##paintProc=subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')
##paintProc.poll() == None
##paintProc.wait() # Doesn't return until MS Paint closes.
##paintProc.poll()


# Doesn't return until MS Paint closes.


##############################################33
##fileObj=open("hello.txt","w")
##fileObj.write("Hola mundo")
##fileObj.close()
##import subprocess
##subprocess.Popen(['start', 'hello.txt'], shell=True) #lo abre
##


##############################################33
#######################COUNTDOWn CON SONIDO CUANDO FINALICE EL TIEMPO
##import datetime,time ,subprocess
##
##timeLeft=60
##
##while timeLeft> 0:
##    print(timeLeft,end="")
##    time.sleep(1)
##    timeLeft=timeLeft-1
##    #TODO : At the end of the countdown ,play a sound file
##subprocess.Popen(["start","alarm.wav"], shell=True)


################################################################




