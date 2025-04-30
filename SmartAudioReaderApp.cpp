#include "SmartAudioReaderApp.h"

#include "SmartAudioReaderApp.h"

SmartAudioReader::SmartAudioReader() {
   
}

void SmartAudioReader::run() {

    string original = reader.readFromFile("test.txt");
    string simp = simplifier.simplify(original);
    speaker.speak(simp);

}
