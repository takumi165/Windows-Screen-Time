import ctypes
import time

from ctypes import windll
from ctypes import wintypes

user32 = windll.user32
kernel32 = windll.kernel32

GetForegroundWindow = user32.GetForegroundWindow
GetCurrentProcessId = kernel32.GetCurrentProcessId()

GetWindowThreadProcessId = user32.GetWindowThreadProcessId

#引数の型を指定
GetWindowThreadProcessId.argtypes = [
    wintypes.HWND,
    wintypes.LPDWORD
]

#PIDを受け取る変数の型を指定
foregroundpid = ctypes.c_ulong(0)

#戻り値の型を指定
GetWindowThreadProcessId.restype = wintypes.DWORD

def main():

    durationtime = 0
    while (True):

        #フォアグラウンドのウィンドウハンドルからPIDを取得する関数を実行(ウィンドウハンドル,変数のポインター)
        GetWindowThreadProcessId(GetForegroundWindow(),ctypes.byref(foregroundpid))

        #現在のPIDを保持する
        beforewindow = foregroundpid.value

        #0秒後に使用しているウィンドウを取得
        time.sleep(1)
        GetWindowThreadProcessId(GetForegroundWindow(),ctypes.byref(foregroundpid))
        print(foregroundpid.value)

        #新たに取得したPIDと保持しているPIDを比較
        afterwindow = foregroundpid.value
        
        if(beforewindow == afterwindow):
            durationtime += 1
            print(f"{foregroundpid.value}を{durationtime}秒間使用しています")
        else:
            durationtime = 0
            print("アプリケーションが変更されました")





if __name__ == "__main__":
    main()