# create_collage_69458
import random

from pip._vendor import requests

import PIL

from PIL import Image,ImageOps
import colage

def create_collage(images):
    for i in range(len(images)):
        images[i] = images[i].resize((600, 600))
        images[i] = ImageOps.expand(images[i],border = 5,fill='black')
    while(True):
        if len(images) == 1:
            return images[0]
        if len(images) == 2:
            return colage.create_collage_2(images)
        if len(images) == 3:
            return colage.create_collage_3(images)

        if len(images) == 4:
            rand = 1
        if len(images) == 5:
            rand = random.randint(1, 2)
        if len(images) == 6 or len(images) == 7:
            rand = random.randint(1, 3)
        if len(images) == 8:
            rand = random.randint(1, 4)
        if len(images) >= 9:
            rand = random.randint(1, 5)

        num = 0
        if rand == 1:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_4(img))
        if rand == 2:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_5(img))
        if rand == 3:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_6(img))
        if rand == 4:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_8(img))
        if rand == 5:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_9(img))

# response = requests.get(url)
# img = Image.open(BytesIO(response.content))

listofimages=[]
# listofimages=[PIL.Image.open('asd.jpg'), PIL.Image.open('sdf.jpg'), PIL.Image.open('vvv.jpg'),PIL.Image.open('asd.jpg'), PIL.Image.open('sdf.jpg'), PIL.Image.open('vvv.jpg'),PIL.Image.open('asd.jpg'), PIL.Image.open('sdf.jpg'), PIL.Image.open('vvv.jpg'),PIL.Image.open('asd.jpg'), PIL.Image.open('sdf.jpg'), PIL.Image.open('vvv.jpg'),PIL.Image.open('asd.jpg'), PIL.Image.open('sdf.jpg'), PIL.Image.open('vvv.jpg'),PIL.Image.open('asd.jpg'), PIL.Image.open('sdf.jpg'), PIL.Image.open('vvv.jpg'),PIL.Image.open('asd.jpg'), PIL.Image.open('sdf.jpg'), PIL.Image.open('vvv.jpg'),PIL.Image.open('asd.jpg'), PIL.Image.open('sdf.jpg'), PIL.Image.open('vvv.jpg'), PIL.Image.open('vvv.jpg'),PIL.Image.open('vvv.jpg') ,PIL.Image.open('vvv.jpg'), PIL.Image.open('vvv.jpg'), PIL.Image.open('vvv.jpg')]

create_collage(listofimages).save("mycolage.jpg")
