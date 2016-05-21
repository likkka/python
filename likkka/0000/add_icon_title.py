from PIL import Image,ImageDraw,ImageFont

im = Image.open("icon.jpg")
# im.show()
w,h = im.size
scale = 0.7
title = "4"
fnt = ImageFont.truetype('simsunb.ttf',w/3)

draw = ImageDraw.Draw(im)
draw.text((w*scale,h*(1-scale)/2),title,font=fnt,fill='RED')
im.show()
im.save('icon2.jpg','jpeg')
