# MusicKaraokeMaker


With this project we can separate vocal and music from any youtube video song.


Packages used

>> pip3 install spleeter
>> pip3 install youtube_dl
>> pip3 install moviepy


Folder structure

 |-songs
 |-output
 |-downloadyt.py



Commands to run 

>>  python3 downloadyt.py 
1) it will ask for youtube url
2) it will ask for output_file_name

>> mv song.mp3 songs/

>> spleeter separate songs/song.mp3 -o output/


>> python3 makevideo.py <imagename>.jpeg <audioname>.wav <outputfilename>.mp4
