import os
import soundfile as sf


# assign directory
directory = 'clips/0237_chunks'

# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    audio = sf.SoundFile(f)
    # contains all the metadata about the wavpack file
    seconds = format(audio.frames / audio.samplerate)
    if float(seconds) < 1 :
        print (f, " = ", seconds)