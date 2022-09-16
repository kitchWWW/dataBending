# databending helper functions

## usage:

To get into the system first run a comand like:
```
convert og.png -resize 1024x1024\! test.png
```
which will put your image into a perfect square, 1024x1024, which is what we'll work with for this.

Then, in the python code, notice at the end, functions:
```
imgToAud("test.png","test1.wav")
```
and 
```
audToImage("test1.wav","test2.png")
```
Run these to do each of the different conversions.


