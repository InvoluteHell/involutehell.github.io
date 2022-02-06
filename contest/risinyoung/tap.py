import time
import cv2
import numpy
import win32gui
import win32ui
import win32con
import win32api
from pyautogui import press
from numba import jit


@jit
def press(key):
    win32api.keybd_event(key,0, 0, 0)
    win32api.keybd_event(key,0, win32con.KEYEVENTF_KEYUP, 0)

@jit
def grab_screen():
    hdesktop = win32gui.GetDesktopWindow()
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    mem_dc.BitBlt((0,0),(width,height),img_dc,(0,0),win32con.SRCCOPY)
    signedIntArray = screenshot.GetBitmapBits(True)
    img = numpy.frombuffer(signedIntArray,dtype='uint8')
    img.shape = (height, width, 4)
    img = img[:,:,:3]
    #screenshot.SaveBitmapFile(mem_dc,'target.bmp')
    img_dc.DeleteDC()
    mem_dc.DeleteDC()
    win32gui.ReleaseDC(hdesktop, desktop_dc)
    win32gui.DeleteObject(screenshot.GetHandle())
    return img

if __name__=="__main__":
    threshold = 0.015
    pdel = 10
    time_delta = 1.8e-2
    time.sleep(10)
    t1 = time.time()
    target = grab_screen()
#	target = cv2.imread('target.bmp')
    target = target[86:1040:2,866:1070:pdel,0]
    template = cv2.imread("template.bmp")
    template = template[::2,::pdel,0]
#	result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
    loc = reversed((numpy.where(result > 1 - threshold)[1]))
    tap = {0:"d", 50:"f", 100:"j", 150:"k"}
    tap1 = [68,70,74,75]
    for x in loc:
        press(tap1[x//5])
    time.sleep(time_delta)
    while(1):
        target = grab_screen()
#		target = cv2.imread('target.bmp')
        target = target[500:1040:2,866:1070:pdel,0]
#		result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
        result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
        loc = reversed((numpy.where(result > 1 - threshold)[1]))
#		loc = reversed((numpy.where(result < threshold)[1]))
        for x in loc:
            press(tap1[x//5])
        time.sleep(time_delta)
        t2 = time.time()
        if(t2-t1 > 20.5):
            break



