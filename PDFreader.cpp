#include "PDFreader.h"

string PDFreader::readFromFile(string file_to_read) {
    string file_contents;
    string str;
    ifstream ins(file_to_read);

    while (getline(ins, str)){
        file_contents += str;
        file_contents.push_back('\n');
    }

    return file_contents;
}