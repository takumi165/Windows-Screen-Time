import ctypes

from ctypes import windll

user32 = windll.user32
kernel32 = windll.kernel32

print(user32)

GetForegroundWindow = user32.GetForegroundWindow()
GetCurrentProcessId = kernel32.GetCurrentProcessId()

print(GetForegroundWindow)
print(GetCurrentProcessId)