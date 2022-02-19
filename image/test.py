from PIL import Image

img = Image.open("test.jpg").convert("P")

print(img.getpixel((14,10)))
