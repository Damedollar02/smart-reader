#ifndef SMART_AUDIO_READER_H
#define SMART_AUDIO_READER_H
#include "PDFreader.h"
#include "TextSimplifier.h"
#include "Speaker.h"


class SmartAudioReader {
    private:

    PDFreader reader;
    TextSimplifier simplifier;
    Speaker speaker;


    public:
    SmartAudioReader();
    void run();

};



#endif