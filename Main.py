# This script is intended to work with Rio-windows-setup-server 
# Netcat is the only dependency

import os
import system
import sys
import subprocess

#Turn off UAC and windows defender
os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
p = subprocess.Popen(["powershell.exe", "Set-MpPreference -DisableRealtimeMonitoring $true"], stdout=sys.stdout)

os.system("cd c:/Rio")
os.system("ncat.exe")

#turn UAC and windows defender back on
p = subprocess.Popen(["powershell.exe", "Set-MpPreference -DisableRealtimeMonitoring $false"], stdout=sys.stdout)
os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f")
