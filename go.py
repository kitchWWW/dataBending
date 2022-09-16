import numpy as np
from PIL import Image
from scipy.io.wavfile import write
from scipy.io.wavfile import read

letters = ['a','b','c','d','e','f','g','h','i','j','k','l']
# letters = ['a']

shapeImage = (1024,1024,3)
shapeAudio = (3145728,)
singleLenSize = 1024*1024*3

def imgToAud(imgName, audName):
	print(imgName)
	img = Image.open(imgName).convert('RGB')
	# convert it to a matrix
	vector = np.asarray(img).reshape(shapeAudio)
	print(vector.dtype)
	print(vector)
	# do something to the vector
	print(vector.shape)

	newv = vector
	samplerate = 44100;

	biggestNumb = np.iinfo(np.int16).max
	newnewv = ((newv / 255.0) * (biggestNumb*2)) - biggestNumb
	write(audName, samplerate, newnewv.astype(np.int16))

def audToImage(audName, imgName):
	print(audName)
	sr, dat = read(audName)
	print(dat)
	if(dat.size > singleLenSize):
		dat = dat[:singleLenSize]
	if(dat.size<singleLenSize):
		print(singleLenSize-dat.size)
		dat = np.pad(dat, (0, singleLenSize-dat.size), 'constant')
	print(dat.size)
	print(singleLenSize)
	dat = (((dat / np.iinfo(np.int16).max) + 1) * (255.0 *10 /2)).round().astype(np.uint8) # np.uint8 vs np.int16 // keeps skin tone same while distoring other colors
	# dat = (((dat / np.iinfo(np.int16).max) + 1) * (255.0)).round().astype(np.int16) # classic distortion / grainy
	# dat = (((dat / np.iinfo(np.int16).max) + 1) * (255.0/2)).round().astype(np.uint8) # TRUE 1:1 MAPPING
	print(dat)

	arr4 = np.asarray(dat).reshape(shapeImage)
	img2 = Image.fromarray(arr4, 'RGB')
	img2.save(imgName)

# for l in letters:
# 	imgToAud("res/"+l+".png","o/o"+l+".wav")

# for l in letters:
# 	for j in range(4):
# 		imgToAud("o/o"+l+str(j+1)+".png","o/o"+l+str(j+1)+".wav")


# for l in letters:
# 	audToImage("o/o"+l+".wav","o/o"+l+"1.png")

# imgToAud("1.png","1r.wav")
# imgToAud("0.png","0.wav")

audToImage("a.wav","a.png")

# audToImage("4.wav","4.png")

