import re, Image, urllib, StringIO

img = urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()

# Image.open requires a file-like object
i = Image.open(StringIO.StringIO(img))

# gray r=g=b and has a period of 7 pixels
row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]
tips =  ''.join(map(chr,ords))
print(''.join(map(chr,map(int, re.findall('\d+', tips)))))
