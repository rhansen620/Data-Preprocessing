from pydub import AudioSegment

audio_file= "1296.wav"
audio = AudioSegment.from_wav(audio_file)
f = open("khmerdata.csv", "r", encoding='utf-16')
lines = f.readlines()[1204:1369] #first line to look at and the last line
list_of_timestamps = [] #and so on in *seconds*

for line in lines:
    tabs = line.split("\t")
    timestamp = int(tabs[4])
    timestamp = int(timestamp)
    list_of_timestamps.append(timestamp)

print (list_of_timestamps)

start = 0
for  idx,t in enumerate(list_of_timestamps):
    #break loop if at last element of list
    if idx == len(list_of_timestamps):
        break

    end = t * 10 #pydub works in millisec
  #  print ("split at [ {}:{}] ms".format(start, end))
    audio_chunk=audio[start:end]
    audio_chunk.export( "audio_chunk_{}.wav".format(end), format="wav")

    start = end #pydub works in millisec

