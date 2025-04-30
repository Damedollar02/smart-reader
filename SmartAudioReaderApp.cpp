
#include "SmartAudioReaderApp.h"
#include <iostream>
#include <string>
#include <cstdlib>

SmartAudioReader::SmartAudioReader() {
   
}

void SmartAudioReader::run() {

    string file;
    cout << "Enter the name of the file you want to simplify: ";
    getline(cin, file);

    string command = "python3 chatgpt_simplifier.py \"" + file + "\"";
    system(command.c_str());
}
