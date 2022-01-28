import time
import pyautogui as pag
from numba import jit
key = ['d', 'f', 'j', 'k']


@jit
def click(num_of_hei, num_of_wid=4, start_x=550, start_y=632, wid=200, hei=200):
    im = pag.screenshot(region=(start_x, start_y - (num_of_hei - 1) * hei, wid * num_of_wid, hei * num_of_hei))
    click_list = []
    for j in reversed(range(num_of_hei)):
        for i in range(num_of_wid):
            pix = im.getpixel((i * wid + 0.8 * wid, j * hei + 0.7 * hei))
            if pix[0] == 255:
                click_list.append(key[i])
    print(click_list)
    pag.press(click_list)


if __name__ == '__main__':
    while True:
        click(5)
        time.sleep(0.04)
