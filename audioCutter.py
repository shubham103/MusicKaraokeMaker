import librosa
import soundfile as sf
audio_file = r'output/song6/vocals.wav'
#read wav data
audio, sr = librosa.load(audio_file, sr= 8000, mono=True)

#print(audio.shape, sr)

clips = librosa.effects.split(audio, top_db=30)
#print(clips)

wav_data = []
for c in clips:
    #print(c)
    data = audio[c[0]: c[1]]
    wav_data.extend(data)
sf.write('new_song6.wav', wav_data, sr)
print("file created")
