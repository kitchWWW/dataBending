# databending helper functions
![alt text](https://github.com/kitchWWW/dataBending/blob/main/z_keep/p_10.png?raw=true)

## usage:

To get into the system first run a comand like:
```
convert og.png -resize 1024x1024\! test.png
```
which will put your image into a perfect square, 1024x1024, which is what we'll work with for this.

NOTE: Make sure to have the `\!` so that your image starts out as the perfect square. Shit gets bad if you don't do that.

Then, in the python code, notice at the end, functions:
```
imgToAud("test.png","test1.wav")
```
and 
```
audToImage("test1.wav","test2.png")
```

To start off, uncomment one of those lines and then run `python go.py` and watch it convert. Make your edits to `test1.wav` in audacity or whatever, then **comment out the first line** (so you don't overwrite your work) and uncomment the second so you can see it converted back into an image. Then do whatever you want with MS paint, and repeat! Happy databending!

![alt text](https://github.com/kitchWWW/dataBending/blob/main/z_keep/p_2.png?raw=true)
