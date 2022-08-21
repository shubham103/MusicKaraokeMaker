# MusicKaraokeMaker


With this project we can separate vocal and music from any youtube video song.


Packages used

$ pip install spleeter
$ pip install youtube_dl


Folder structure

+ --- songs/
   |
   -- output/
   |
   -- downloadyt.py


Commands to run 

$ python3 downloadyt.py 
------> it will ask for youtube url
------> it will ask for output_file_name

$ mv song.mp3 songs/

$ spleeter separate songs/song.mp3 -o output/
