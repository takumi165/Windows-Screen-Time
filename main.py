import ctypes

from ctypes import windll
from ctypes import wintypes

user32 = windll.user32
kernel32 = windll.kernel32

print(user32)

GetForegroundWindow = user32.GetForegroundWindow()
GetCurrentProcessId = kernel32.GetCurrentProcessId()

print(GetForegroundWindow)
print(GetCurrentProcessId)

GetWindowThreadProcessId = user32.GetWindowThreadProcessId
GetWindowThreadProcessId.argtypes = [
    wintypes.HWND,
    wintypes.LPDWORD
]

pid = ctypes.c_ulong(0)

GetWindowThreadProcessId.restype = wintypes.DWORD

GetWindowThreadProcessId(GetForegroundWindow,ctypes.byref(pid))

print(GetWindowThreadProcessId(GetForegroundWindow,ctypes.byref(pid)))