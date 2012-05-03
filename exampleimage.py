from PIL import Image, ImageDraw, ImageFont


im = Image.new(mode='RGB', size=(400, 200))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('arial.ttf', 12)
draw.text((20, 100), 'EXAMPLE TEXT', font=font, fill='#ffffff')
f = open('example.png', 'wb')
im.save(f)
