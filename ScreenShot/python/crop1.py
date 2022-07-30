from PIL import Image

img = Image.open("1527256533096079361.png")
box = (0, 0, 1120, 740)
img2 = img.crop(box)
img2.save('myimage_cropped.png')