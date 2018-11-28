import PIL

from PIL import Image,ImageOps

def create_collage_9(imgs):
    target_img = Image.new("RGB", (600, 600))

    for i in range(9):
        imgs[i] = imgs[i].resize((200, 200))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (0, 200))
    target_img.paste(imgs[2], (200, 0))
    target_img.paste(imgs[3], (200, 200))
    target_img.paste(imgs[4], (400, 0))
    target_img.paste(imgs[5], (0, 400))
    target_img.paste(imgs[6], (200, 400))
    target_img.paste(imgs[7], (400, 200))
    target_img.paste(imgs[8], (400, 400))

    return target_img

def create_collage_5(imgs):
    target_img = Image.new("RGB", (600, 600))

    imgs[0] = imgs[0].resize((300, 300))
    target_img.paste(imgs[0], (0, 0))
    imgs[1] = imgs[1].resize((300, 300))
    target_img.paste(imgs[1], (0, 300))
    imgs[2] = imgs[2].resize((300, 200))
    target_img.paste(imgs[2], (300, 0))
    imgs[3] = imgs[3].resize((300, 200))
    target_img.paste(imgs[3], (300, 200))
    imgs[4] = imgs[4].resize((300, 200))
    target_img.paste(imgs[4], (300, 400))

    return target_img

def create_collage_4(imgs):
    target_img = Image.new("RGB", (600, 600))

    for i in range(4):
        imgs[i] = imgs[i].resize((300, 300))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (0, 300))
    target_img.paste(imgs[2], (300, 0))
    target_img.paste(imgs[3], (300, 300))

    return target_img


def create_collage_6(imgs):
    target_img = Image.new("RGB", (600,600))

    for i in range(5):
        imgs[i+1]=imgs[i+1].resize((200, 200))

    imgs[0]=imgs[0].resize((400,400))
    target_img.paste(imgs[0], (0,0))
    target_img.paste(imgs[1], (0,400))
    target_img.paste(imgs[2], (400,0))
    target_img.paste(imgs[3], (400,200))
    target_img.paste(imgs[4], (400,400))
    target_img.paste(imgs[5], (200,400))
    return target_img

def create_collage_8(imgs):
    target_img = Image.new("RGB", (600, 600))

    imgs[0] = imgs[0].resize((200, 100))
    target_img.paste(imgs[0], (0, 0))
    imgs[1] = imgs[1].resize((200, 250))
    target_img.paste(imgs[1], (0, 100))
    imgs[2] = imgs[2].resize((300, 250))
    target_img.paste(imgs[2], (0, 350))
    imgs[3] = imgs[3].resize((300, 200))
    target_img.paste(imgs[3], (200, 0))
    imgs[4] = imgs[4].resize((100, 150))
    target_img.paste(imgs[4], (200, 200))
    imgs[5] = imgs[5].resize((100, 200))
    target_img.paste(imgs[5], (500, 0))
    imgs[5] = imgs[5].resize((300, 200))
    target_img.paste(imgs[5], (300, 200))
    imgs[5] = imgs[5].resize((300, 200))
    target_img.paste(imgs[5], (300, 400))
    return target_img

def create_collage_2(imgs):
    target_img = Image.new("RGB", (1200, 600))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (600, 0))

    return target_img

def create_collage_3(imgs):
    target_img = Image.new("RGB", (1800, 600))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (600, 0))
    target_img.paste(imgs[2], (1200, 0))

    return target_img
# listofimages=['6966686921.jpg', '6966686922.jpg', '6966686923.jpg', '6966686924.jpg', '6966686925.jpg', '6966686921.jpg','6966686921.jpg', '6966686922.jpg', '6966686923.jpg', '6966686924.jpg', '6966686925.jpg', '6966686921.jpg']
# listofimages_frame=frame_to_image(listofimages, 1, 'black')
# create_collage_6(listofimages_frame[:6], 'test_collage1.jpg')
# create_collage_9(listofimages_frame[:9], 'test_collage2.jpg')
# create_collage_4(listofimages_frame[:4], 'test_collage3.jpg')
# create_collage_5(listofimages_frame[:5], 'test_collage4.jpg')
# create_collage_8(listofimages_frame[:8], 'test_collage5.jpg')