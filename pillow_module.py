# installation of pillow library
# change the image extension
# resize image file
# resize multiple images using  for loop
# sharpness
# brightness
# color
# Contrast
# Image blur , GauuianBlur
from PIL import Image , ImageEnhance , ImageFilter
import os

# how can we change extension of image
image1 = Image.open('dog1.jpg')
# image1.save('dog1.pdf')
# You can show the image
# image1.show()

# image resize
# MAX_SIZE = (250,250)
# image1.thumbnail(MAX_SIZE)
# image1.save('dog1small.jpg')

# if we want to convert multiple files
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         image1 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         image1.save(f'{filename}.png')


# #  Mow we understand sharpness
# enhancer = ImageEnhance.Sharpness(image1)
# enhancer.enhance(2).save('dog1edited.jpg')
# 0 : blurry
# 1 : original image
# 2: image with increase sharpness

# now we see color class
# enhancer = ImageEnhance.Color(image1)
# enhancer.enhance(2).save('dog1edited.jpg')

# # now we see brightness 
# enhancer = ImageEnhance.Brightness(image1)
# enhancer.enhance(1).save('dog1edited.jpg')


# now see contrast
# enhancer = ImageEnhance.Contrast(image1)
# enhancer.enhance(2).save('dog1edited.jpg')

# image blur

image1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog1edit.jpg')