# This script is intended to work with Rio-windows-setup-server 
# Netcat is the only dependency

import os
import system

#Turn off UAC
os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
os.system("cd c:/Rio")
os.system("ncat.exe")

#turn UAC back on
os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f")
