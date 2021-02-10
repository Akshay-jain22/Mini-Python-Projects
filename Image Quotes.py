from PIL import Image, ImageDraw

quote = input("Enter any Quote : ")

background = Image.new('RGB',(200,200),color=(3,252,232))

d = ImageDraw.Draw(background)
d.text((60, 90), quote, fill=(255,255,255))

background.show()

background.save("images/quote.png")