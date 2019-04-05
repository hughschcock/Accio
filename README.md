# Accio
Usage : python3 Accio.py PATH [-f FILENAME | -x EXT1,EXT2... | -t (pictures|videos)| -d destination | -c]


PATH=path to spider search with os.walk(PATH)
-t,  --type=images|videos 
-f,  --file=FILENAME    search for a file and copy it to the current working directory
-x,  --extension=EXT... search for specific file extension  
-h,  --help display this help text and exit
-d,  --destination       destination to copy/move file instead of .
-c,  --copy              copy instead of move
