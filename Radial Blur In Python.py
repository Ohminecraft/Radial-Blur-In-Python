import ctypes
from ctypes import *
from ctypes.wintypes import RECT

# Windll
Rect = RECT()
BitBlt = windll.gdi32.BitBlt
PlgBlt = windll.gdi32.PlgBlt
CreateCompatibleDC = windll.gdi32.CreateCompatibleDC
CreateCompatibleBitmap = windll.gdi32.CreateCompatibleBitmap
SelectObject = windll.gdi32.SelectObject
DeleteObject = windll.gdi32.DeleteObject
DeleteDC = windll.gdi32.DeleteDC
GetDC = windll.user32.GetDC
GetWindowRect = windll.user32.GetWindowRect
GetDesktopWindow = windll.user32.GetDesktopWindow
AlphaBlend = windll.msimg32.AlphaBlend
GetSystemMetrics = windll.user32.GetSystemMetrics
Sleep = windll.kernel32.Sleep
#

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)

class BLENDFUNCTION(ctypes.Structure):
    _fields_ = [('BlendOp', c_byte),
                ('BlendFlags', c_byte),
                ('SourceConstantAlpha', c_byte),
                ('AlphaFormat', c_byte)]

BlendFunction = BLENDFUNCTION()
BlendFunction.BlendOp = 0
BlendFunction.BlendFlags = 0
BlendFunction.SourceConstantAlpha = 50
BlendFunction.AlphaFormat = 0

class POINT(ctypes.Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

ThreePoint = POINT * 3

while True:
    Rect = RECT()
    hwnd = GetDesktopWindow()
    GetWindowRect(hwnd, pointer(Rect))
    top = Rect.top
    bottom = Rect.bottom
    left = Rect.left
    right = Rect.right
    hdc = GetDC(0)
    mhdc = CreateCompatibleDC(hdc);
    hbit = CreateCompatibleBitmap(hdc, w, h);
    holdbit = SelectObject(mhdc, hbit);
    if rand(2) == 1:
        point = ThreePoint((left + 10, top - 10),(right + 10, top + 10),(left - 10, bottom - 10))
    else:
        point = ThreePoint((left - 10, top + 10),(right - 10, top - 10),(left + 10, bottom + 10))
    PlgBlt(mhdc, point, hdc, left, top, (right - left), (bottom - top), 0, 0, 0);
    AlphaBlend(hdc, 0, 0, w, h, mhdc, 0, 0, w, h, BlendFunction);
    SelectObject(mhdc, holdbit)
    DeleteObject(holdbit)
    DeleteObject(hbit)
    DeleteDC(mhdc)
    DeleteDC(hdc)
    Sleep(50)
