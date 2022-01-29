#include <Afxwin.h>
#include <Windows.h>
#include <iostream>
#pragma comment (lib, "User32.lib")

int red, green, blue;
int black = 0;
int x=725, y=860;

int main(void) {
	HWND hWnd = ::GetDesktopWindow();
	HDC hdc = ::GetDC(hWnd);	
	for (int i = 0; i < 1;) {
		COLORREF pixel = ::GetPixel(hdc, x, y);
		if (pixel != CLR_INVALID) {
		red = GetRValue(pixel);
		green = GetGValue(pixel);
		blue = GetBValue(pixel);
			if (red == black && green == black && blue == black) {
				if (x == 725) {
					keybd_event('D', 0, 0, 0);
						Sleep(20);
				}
				else if (x == 890) {
					keybd_event('F', 0, 0, 0);
						Sleep(20);
				}
				else if (x == 1055) {
					keybd_event('J', 0, 0, 0);
						Sleep(20);
				}
				else if (x == 1220) {
					keybd_event('K', 0, 0, 0);
						Sleep(20);
				}
			}else if(x!=1220) {
				x += 165;
			}else {
				x = 725;
			}
		}	
	}
	std::cout << "D:" << numd << " F:" << numf << " J:" << numj << " K:" << numk<<std::endl;
	std::cout << "SUM_CLICK_NUM=" << num;
	system("PAUSE");
	return 0;
}

