#ifndef SMART_AUDIO_READER_H
#define SMART_AUDIO_READER_H
#include "PDFreader.h"




class SmartAudioReader {
    private:

    PDFreader reader;


    public:
    SmartAudioReader();
    void run();

};



#endif