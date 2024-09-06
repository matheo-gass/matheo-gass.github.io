#----------------------------------------------------------------|
#                                                                |
#	Little program I made for generate texts with DKC2 Fonts.|
#	I kinda doesn't like Python programming, but I have to admit it's very efficient with image manipulation libraries.
#	Feel free to download it and to re use it anywhere you want.
#	I'll try to leave a maximum of comments to explain how I do and how it works.
#                                                                |
#----------------------------------------------------------------|

import sys # Used for parse arguments when calling file
from PIL import Image # Importing Image method for image creation, and manipulation
text=sys.argv[1] # Wanted text
type=sys.argv[2] # Type of text normal/big
if type=="big":
	sheet=Image.open("/opt/lampp/htdocs/dkc2world/files/graphics/.texts/big-font.png") # Path of the big font sheet
	letters=["A:00","B:10","C:20","D:30","E:40","F:50","G:60","H:70","I:80","J:90","K:a0","L:b0","M:c0","N:d0","O:e0","P:f0","Q:01","R:11","S:21","T:31","U:41","V:51","W:61","X:71","Y:81","Z:91","0:02","1:12","2:22","3:32","4:42","5:52","6:62","7:72","8:82","9:92","Â","À","È","Ö","Û","!",".","'",",",":","-","/","%","&"] # Letters indexes and positions, letters are 8 by 16
	x_size=0
	lines=[]
	lines_nb=0
	y_size=1
	for letter in text: # Defining text size
		print(letter)
		if letter=='\n':
			lines_nb+=1
			y_size+=1
			x_size=0
		else:
			x_size+=1
			lines.append(x_size)
	print(lines)
