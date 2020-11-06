from tkinter import *
from tkinter import filedialog
import time,sys,os
import pathlib
import pyautogui
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def takeScreenshot():
  screenshot = pyautogui.screenshot()
  timestr = time.strftime("%Y%m%d-%H%M%S")
  desktop = pathlib.Path.home() / 'Desktop'
  print(timestr)
  print(desktop)
  file = "{}\{}.png".format(desktop,timestr)
  screenshot.save(file)
  
root =Tk()
iconres= resource_path("logo.png")
icon = PhotoImage(file = iconres)
root.iconphoto(False, icon)
root.title('screenShoot')
root.resizable(0,0)
root.geometry('100x30+0+0')
root.attributes('-toolwindow', True)
root.attributes('-topmost', True)
root['bg'] = '#212121'
Button(root,text = 'ScreenShot',bg='#303030',fg='white',command = takeScreenshot).pack()
root.mainloop()
