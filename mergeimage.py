import random

from PIL import Image,ImageOps
import colage


def cut_image(img):
   im = Image.open(img)
   x=max(im.size)
   y=min(im.size)
   z=x-y
   if im.size[0]>im.size[1]:
       region = im.crop((z/2,0, y+(z/2) , y ))
   else:
       region = im.crop((0 ,z/2, y,y+(z/2)))
   return region

def create_collage(images):
    for i in range(len(images)):
        # images[i] = images[i].resize((600, 600))
        images[i] = cut_image(images[i])

        images[i] = ImageOps.expand(images[i],border = 5,fill='black')
    while(True):
        if len(images) == 0:
            return None
        if len(images) == 1:
            return images[0]
        if len(images) == 2:
            return colage.create_collage_2(images)
        if len(images) == 3:
            return colage.create_collage_3(images)

        rand = 1
        if len(images) == 5:
            rand = random.randint(1, 2)
        if len(images) == 6 or len(images) == 7:
            rand = random.randint(1, 3)
        if len(images) == 8:
            rand = random.randint(1, 4)
        if len(images) >= 9:
            rand = random.randint(1, 5)

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